from instapy import InstaPy
from instapy import smart_run
import random

# Session credentials
Git removed
# Session initializer
session = InstaPy(username="foo", password="oof", headless_browser=True, want_check_browser=False)

# Session runner
with smart_run(session):
    # Hashtags to explore
    hashtags = ['travelcouples', 'travelcommunity', 'passionpassport',
                'travelguide', 'travelbloggers', 'letsgoeverywhere',
                'travelislife', 'beautifuldestinations',
                'travelgram', 'sunsetporn', 'travelling', 'instatraveling',
                'travelingram', 'skyporn', 'traveler', 'sunrise',
                'sunsetlovers', 'sunset_pics', 'ilovetravel',
                'photographyoftheday', 'sunsetphotography',
                'explorenature', 'exploring_shotz',
                'landscapehunter', 'earthfocus', 'ig_shotz', 'ig_nature', 'discoverearth',
                'photography', 'picoftheday', 'nofilter', 'visitportugal', 'instatravel',
                'travelphotography', 'photooftheday', 'aveirolovers', 'porto', 'lisbon']
    
    # Shufle hashtags and pick 10
    random.shuffle(hashtags)
    my_hashtags = hashtags[:10]

    #Comments
    my_comments = ['What an amazing shot @{}! :heart_eyes:', 'Nice shot! @{}', 'Wonderful photo @{}!! :heart_eyes:', '@{} Love it!! :wink: :hearth:','This is awesome @{}!! :heart_eyes: ','Great capture @{}!! :smiley: :wink:',
                   'I love ur profile @{}!!  :smiley: :thumbsup:', '@{}:revolving_hearts::revolving_hearts:', '@{}:fire::fire:', '@{} Amazing photo :fire:', 'Nice pic @{} :fire:']
    
# general settings
    session.set_dont_like(['sad', 'rain', 'depression', 'covid', 'racism'])
    session.set_do_follow(enabled=True, percentage=30, times=1)
    session.set_do_comment(enabled=True, percentage=40)
    session.set_comments(my_comments)

    session.set_do_like(True, percentage=50)
    session.set_delimit_liking(enabled=True, max_likes=90, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=5000,
                                    max_following=5000,
                                    min_followers=100,
                                    min_following=50)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "follows"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=30,
                                 peak_likes_daily=600,
                                 peak_comments_hourly=10,
                                 peak_comments_daily=200,
                                 peak_follows_hourly=50,
                                 peak_follows_daily=None)

    session.set_user_interact(amount=1, randomize=False, percentage=35)

    # activity
    session.unfollow_users(amount=10, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=501)
    session.unfollow_users(amount=10, instapy_followed_enabled=True, instapy_followed_param="all",
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=501)
    session.like_by_tags(my_hashtags, amount=30, media=None)

    """ Joining Engagement Pods...
    """
    session.join_pods()
