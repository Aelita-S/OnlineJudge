from utils.api.tests import APITestCase

from .models import Announcement


class AnnouncementAdminTest(APITestCase):
    def setUp(self):
        self.user = self.create_super_admin()
        self.url = self.reverse("announcement_admin_api")

    def test_announcement_list(self):
        response = self.client.get(self.url)
        self.assertSuccess(response)

    def create_announcement(self):
<<<<<<< HEAD
        return self.client.post(self.url, data={"title": "test", "content": "test", "visible": True, "istop": False})
=======
        return self.client.post(self.url, data={"title": "test", "content": "test", "visible": True,"istop": False})
>>>>>>> d4aeab3bb0f192410e824168410151dae697eb10

    def test_create_announcement(self):
        resp = self.create_announcement()
        self.assertSuccess(resp)
        return resp

    def test_edit_announcement(self):
        data = {"id": self.create_announcement().data["data"]["id"], "title": "ahaha", "content": "test content","visible": False,"istop": True}
        resp = self.client.put(self.url, data=data)
        self.assertSuccess(resp)
        resp_data = resp.data["data"]
        self.assertEqual(resp_data["title"], "ahaha")
        self.assertEqual(resp_data["content"], "test content")
        self.assertEqual(resp_data["visible"], False)
<<<<<<< HEAD
        self.assertEqual(resp_data["istop"], False)
=======
	self.assertEqual(resp_data["istop"], False)
>>>>>>> d4aeab3bb0f192410e824168410151dae697eb10

    def test_delete_announcement(self):
        id = self.test_create_announcement().data["data"]["id"]
        resp = self.client.delete(self.url + "?id=" + str(id))
        self.assertSuccess(resp)
        self.assertFalse(Announcement.objects.filter(id=id).exists())


class AnnouncementAPITest(APITestCase):
    def setUp(self):
        self.user = self.create_super_admin()
<<<<<<< HEAD
        Announcement.objects.create(title="title", content="content", visible=True, istop=False, created_by=self.user)
=======
        Announcement.objects.create(title="title", content="content", visible=True, istop=False,  created_by=self.user)
>>>>>>> d4aeab3bb0f192410e824168410151dae697eb10
        self.url = self.reverse("announcement_api")

    def test_get_announcement_list(self):
        resp = self.client.get(self.url)
        self.assertSuccess(resp)
