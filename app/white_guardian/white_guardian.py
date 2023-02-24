import datetime

from pymysql import connect

from settings import DATABASES

connection = connect(
        host=DATABASES.DB_TOPICS.HOST.value,
        user=DATABASES.DB_TOPICS.USERNAME.value,
        password=DATABASES.DB_TOPICS.PASSWORD.value,
        database=DATABASES.DB_TOPICS.DATABASE.value,
        port=int(DATABASES.DB_TOPICS.PORT.value),
    )


def new_id():
    query = f'SELECT MAX(id) FROM ai_content'
    with connection.cursor() as cursor:
        cursor.execute(query)
        id_hiden_in_tuple = cursor.fetchone()
        id_from_tuple = id_hiden_in_tuple[0]
        return int(id_from_tuple) + 1


def new_topic(topic_title, topic_text):
    query = f'INSERT INTO ai_content (`id`, `title`, `introtext`, `fulltext`) VALUES ({new_id()}, {topic_title}, "{topic_text[:30]}...", "{topic_text}")'
    print(query)
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()

# class Topic(DBEntity):
#
#     def __init__(
#             self,
#             id,
#             asset_id,
#             title,
#             alias,
#             introtext,
#             fulltext,
#             state,
#             catid,
#             created,
#             created_by,
#             created_by_alias,
#             modified,
#             modified_by,
#             checked_out,
#             checked_out_time,
#             publish_up,
#             publish_down,
#             images,
#             urls,
#             attribs,
#             version,
#             ordering,
#             metakey,
#             metadesc,
#             access,
#             hits,
#             metadata,
#             featured,
#             language,
#             note
#     ):
#         self.id = id
#         self.asset_id = asset_id
#         self.title = title
#         self.alias = alias
#         self.introtext = introtext
#         self.fulltext = fulltext
#         self.state = state
#         self.catid = catid
#         self.created = created
#         self.created_by = created_by
#         self.created_by_alias = created_by_alias
#         self.modified = modified
#         self.modified_by = modified_by
#         self.checked_out = checked_out
#         self.checked_out_time = checked_out_time
#         self.publish_up = publish_up
#         self.publish_down = publish_down
#         self.images = images
#         self.urls = urls
#         self.attribs = attribs
#         self.version = version
#         self.ordering = ordering
#         self.metakey = metakey
#         self.metadesc = metadesc
#         self.access = access
#         self.hits = hits
#         self.metadata = metadata
#         self.featured = featured
#         self.language = language
#         self.note = note
