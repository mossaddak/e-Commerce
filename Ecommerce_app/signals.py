from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed
from .models import Products,ProductREVIEWS,ProductOrder
from user_profile.models import Follow, User
from notification.models import Notification

@receiver(post_save, sender=Products)
def send_notification_to_followers_when_product_added(instance, created, *args, **kwargs):
    if created:
        followers = instance.user.followers.all()

        for data in followers:
            follower = data.followed_by

            if not data.muted:
                Notification.objects.create(
                    content_object = instance,
                    user = follower,
                    text = f"{ instance.user.username } added a new product.",
                    notification_types = "Product"
                    )


#folowing purpose
@receiver(post_save, sender=Follow)
def send_notification_to_user_when_someone_followed(instance, created, *args, **kwargs):
    if created:
        followed = instance.followed
 
        if not instance.muted:
            Notification.objects.create(
                content_object = instance,
                user = followed,
                text = f"{ instance.followed_by.username } started following you",
                notification_types = "Follow"
                )

