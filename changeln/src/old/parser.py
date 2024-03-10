# import re
#
# import git
# from natsort import natsorted
#
#
# class Parser:
#     def __init__(self, path):
#         self.path = path
#         self.repo = git.Repo(path)

#     def ln_list_tags_commits(self, find_tags):
#         result_tags = []
#
#         list_tags = self.ln_list_tags(find_tags)
#         if list_tags:
#             to = 'HEAD'
#             tag = None
#             for tag in list_tags:
#                 data = list(self.repo.iter_commits('{}...{}'.format(tag, to), no_merges=True))
#
#                 result_tags.append(dict(
#                     to=('TAG', 'HEAD')[to == 'HEAD'],
#                     tag=(to, None)[to == 'HEAD'],
#                     data=data
#                 ))
#                 to = tag
#
#             if tag is not None:
#                 result_tags.append(dict(
#                     to='TAG',
#                     tag=tag,
#                     data=list(self.repo.iter_commits(tag, no_merges=True))
#                 ))
#
#         return result_tags
#
#     def ln_list_groups(self, groups, find_tags):
#         result_tags = self.ln_list_tags_commits(find_tags)
#         result = []
#         for tag in result_tags:
#             commits = dict()
#             for item in tag['data']:
#                 for message in item.message.split('\n'):
#                     for index in groups:
#                         if index not in commits:
#                             commits[index] = []
#                         optional = re.findall(groups[index], message)
#                         if optional:
#                             commits[index].append(dict(
#                                 optional=optional[0],
#                                 commit=git.Commit(
#                                     item.repo,
#                                     item.binsha,
#                                     tree=item.tree,
#                                     author=item.author,
#                                     authored_date=item.authored_date,
#                                     author_tz_offset=item.author_tz_offset,
#                                     committer=item.committer,
#                                     committed_date=item.committed_date,
#                                     committer_tz_offset=item.committer_tz_offset,
#                                     message=message.strip(),
#                                     parents=item.parents,
#                                     encoding=item.encoding,
#                                     gpgsig=item.gpgsig
#                                 )
#                             ))
#             for index in groups:
#                 if index in commits:
#                     tag[index] = commits[index]
#                 else:
#                     tag[index] = []
#             result.append(tag)
#         return result