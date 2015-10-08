#-*-coding:utf-8-*-
#二分查找是否存在[百度百科](http://baike.baidu.com/link?url=hYlEnKdwa1nQ6QQ7Eo8_zYILfzET-O0ZXXztpNJXcyexgkSqLo509fM_Ix6HVp2JK_Yai5Ka0YSDLucGLhm4Jq)
def binarySearch(lists, select):
    is_none = False
    if lists != []:
        cen_num = len(lists) / 2
        tlag = lists[cen_num]
        gt_list = lists[0:cen_num]
        lt_list = lists[cen_num + 1:]

        if tlag == select:
            is_none = True
            return is_none
        elif tlag > select:
            is_se = binarySearch(gt_list, select)
            if not is_se:
                return binarySearch(lt_list, select)
            else:
                return False
            return is_none
        elif tlag < select:
            is_se = binarySearch(lt_list, select)
            if not is_se:
                return binarySearch(gt_list, select)
            else:
                return True
    return is_none



print binarySearch([1, 2, 3, 4, 5], 4)
