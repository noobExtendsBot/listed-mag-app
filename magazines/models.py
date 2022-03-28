from django.db import models
from listed.settings import MEDIA_ROOT
from django.db.models.signals import post_save
from django.dispatch import receiver
import zipfile
import os
# Create your models here.


class MagazinePost(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='magazines/thumbnails/')
    document = models.FileField(upload_to='magazines/epub/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.TextField(default=None, null=True)

    def save(self, force_insert=False, force_update=False):
        dir_name = MEDIA_ROOT + "/magazines/epub/"+ str(self.title)
        path_to_zip_file = MEDIA_ROOT + "/magazines/epub/" + str(self.document.name)
        directory_to_extract_to = MEDIA_ROOT + "/magazines/epub/" + str(self.title)
        # print(directory_to_extract_to)
        print("Inside try")
    
        if not os.path.exists(dir_name):
        # print("Inside make dir")
            os.makedirs(dir_name)
            with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
                zip_ref.extractall(directory_to_extract_to)
                dir_list = [name for name in os.listdir(directory_to_extract_to)]
                # print(dir_list)
                if "META-INF" in dir_list:
                    dir_list.remove("META-INF")
                if "OEBPS" in dir_list:
                    dir_name = dir_name+"/"+"OEBPS"
                    os.chdir(dir_name)
                    print(dir_name," trying path")
                    print(os.getcwd())
                    onlyfiles = [f for f in os.listdir(dir_name)]
                    print(onlyfiles)
                    for i in onlyfiles:
                        if i == "package.opf":
                            dir_name = dir_name+"/"+str(i)
                            print("working bitch", dir_name+"/"+str(i))
                            self.file = dir_name
                            break
        super(MagazinePost, self).save(force_insert, force_update)
    def __str__(self):
        return self.title
    

# @receiver(post_save, sender=MagazinePost, dispatch_uid="update_magazines")
# def update_magazine(sender, instance, created, **kwargs):
#     dir_name = MEDIA_ROOT + "/magazines/epub/"+ str(instance.title)
#     path_to_zip_file = MEDIA_ROOT + "/" + str(instance.document.name)
#     directory_to_extract_to = MEDIA_ROOT + "/magazines/epub/" + str(instance.title)
#     # print(directory_to_extract_to)
#     print("Inside try")
    
#     if not os.path.exists(dir_name):
#     # print("Inside make dir")
#         os.makedirs(dir_name)
#         with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
#             zip_ref.extractall(directory_to_extract_to)
#             dir_list = [name for name in os.listdir(directory_to_extract_to)]
#             # print(dir_list)
#             if "META-INF" in dir_list:
#                 dir_list.remove("META-INF")
#             if "OEBPS" in dir_list:
#                 dir_name = dir_name+"/"+"OEBPS"
#                 os.chdir(dir_name)
#                 print(dir_name," trying path")
#                 print(os.getcwd())
#                 onlyfiles = [f for f in os.listdir(dir_name)]
#                 print(onlyfiles)
#                 for i in onlyfiles:
#                     if i == "package.opf":
#                         dir_name = dir_name+"/"+str(i)
#                         print("working bitch", dir_name+"/"+str(i))
#                         instance.file = dir_name
#                         break
#     instance.save()
#     # m = MagazinePost.objects.get(title=self.title)
#     # m.description = path
#     # m.save()
#     # print(instance.description)
    
#     # try:
#     #     pass
#     # except Exception as e:
#     #     print(e)
    

