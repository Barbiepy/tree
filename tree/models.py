from django.core.validators import MinValueValidator
from django.db import models


class ItemManager(models.Manager):

    def get_detailed_menu(self, pk):
        """
        Получить развернутое меню по переданному pk пункта,
        развернуты будут все элементы выше пункта и один уровень ниже
        :param pk:
        :return: queryset
        """

        return self.raw("""
        WITH RECURSIVE r AS (
          SELECT 
            id, 
            parent_id, 
            name, 
            depth_level 
          from 
            tree_item 
          where 
            parent_id = %s 
            or parent_id in (
              select 
                parent_id 
              from 
                tree_item 
              where 
                id = %s
            ) 
            or id = %s 
          UNION 
          SELECT 
            tree_item.id, 
            tree_item.parent_id, 
            tree_item.name, 
            tree_item.depth_level 
          from 
            tree_item 
            join r on r.parent_id = tree_item.id
        ) 
        SELECT 
          id, 
          name, 
          depth_level 
        FROM 
          r 
        ORDER BY 
          id;
        """, [pk, pk, pk])


class Item(models.Model):

    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')
    name = models.CharField('Название', max_length=30)
    depth_level = models.IntegerField('Уровень', validators=[MinValueValidator(0)])
    objects = ItemManager()

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.depth_level = self.parent.depth_level + 1 if self.parent else 0
        super().save(*args, **kwargs)
