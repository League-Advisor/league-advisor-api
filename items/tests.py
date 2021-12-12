
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status 
from rest_framework.test import APITestCase


from .models import Item

class ItemModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_item = Item.objects.create(
        item_id= 1001,
        name= "Boots",
        description= "<mainText><stats><attention>25</attention> Move Speed</stats></mainText><br>",
        plaintext= "Slightly increases Movement Speed",
        image= "http://ddragon.leagueoflegends.com/cdn/11.24.1/img/item/1001.png",
        gold= 300,
        tags= "['Boots']"
        )
        test_item.save()

    def test_blog_content(self):
        item = Item.objects.get(item_id=1001)

        self.assertEqual(item.name, "Boots")
        self.assertEqual(item.gold, 300)

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('item_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_item = Item.objects.create(
           
            item_id= 1001,
            name= "Boots",
            description= "<mainText><stats><attention>25</attention> Move Speed</stats></mainText><br>",
            plaintext= "Slightly increases Movement Speed",
            image= "http://ddragon.leagueoflegends.com/cdn/11.24.1/img/item/1001.png",
            gold= 300,
            tags= "['Boots']"  
        )
        test_item.save()

        response = self.client.get(reverse('item_detail', args=[1001]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,{
            'item_id':test_item.item_id,
            "name": test_item.name,
            "description" :test_item.description,
            "plaintext": test_item.plaintext,
            "image": test_item.image,
            "gold": test_item.gold,
            "tags": test_item.tags,
     
        })


#     def test_create(self):
#         test_user = get_user_model().objects.create_user(username='tester',password='pass')
#         test_user.save()

#         url = reverse('book_list')
#         data = {
#             "name":"Testing is Fun!!!",
#             "description":"when the right tools are available",
#             "publisher":test_user.id,
#         }

#         response = self.client.post(url, data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

#         self.assertEqual(Book.objects.count(), 1)
#         self.assertEqual(Book.objects.get().name, data['name'])

#     def test_update(self):
#         test_user = get_user_model().objects.create_user(username='tester',password='pass')
#         test_user.save()

#         test_book = Book.objects.create(
#             publisher = test_user,
#             name = 'Title of Blog',
#             description = 'Words about the blog'
#         )

#         test_book.save()

#         url = reverse('book_detail',args=[test_book.id])
#         data = {
#             "name":"Testing is Still Fun!!!",
#             "publisher":test_book.publisher.id,
#             "description":test_book.description,
#         }

#         response = self.client.put(url, data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_200_OK, url)

#         self.assertEqual(Book.objects.count(), test_book.id)
#         self.assertEqual(Book.objects.get().name, data['name'])


#     def test_delete(self):
#         """Test the api can delete a book."""

#         test_user = get_user_model().objects.create_user(username='tester',password='pass')
#         test_user.save()

#         test_book = Book.objects.create(
#             publisher = test_user,
#             name = 'Title of Blog',
#             description = 'Words about the blog'
#         )

#         test_book.save()

#         book = Book.objects.get()

#         url = reverse('book_detail', kwargs={'pk': book.id})


#         response = self.client.delete(url)

#         self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)

