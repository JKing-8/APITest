from xsj_event_info import *

base_expect = {'os',
               'os_version',
               'browser',
               'browser_version',
               'getIp',
               'ip',
               'client_time',
               'create_time',
               'stop_time',
               'date',
               'uniqid',
               'url',
               'referer_url',
               'page',
               'page_type',
               'title',
               'screen_height',
               'screen_width',
               'sem',
               'sem_kid',
               'sem_type',
               'sid',
               'event',
               'click_type',
               'uid',
               'vip_type',
               'is_pic_charged',
               'is_video_charged',
               'pic_plan',
               'video_plan',
               'user_type',
               'act_layer',
               'user_level',
               }

event_is_download = {
    'order_status',
    'click_type',
    'resourceType',
    'is_demo',
    'license',
    'file_image_t',
    'file_video_t',
    'imageid_xsj',
    'videoid_xsj',
    'source_id',
    'author_uid',
    'batchDownloa',
}

event_is_view = {
    'click_type',
    'uid',
    'vip_type',
    'is_pic_charged',
    'is_video_charged',
    'pic_plan',
    'video_plan',
    'act_layer',
    'user_level',
}

event_is_order = {
    'order_status',
    'pay_type',
    'license',
    'pan_ver',
    'order_price',
    'order_no',
}

event_is_search = {
    'search_type',
    'search_cont',
    'resourceType',
    'pic_screen',
    'video_resolution',
    'cont_screen',
    'character_srceen',
    'format_screen',
    'direction_screen',
    'is_boutique',
    'order_screen',
}


class DiffExpectVsXsjResult:
    def __init__(self) -> None:
        self.base_set = base_expect
        self.event_is_download = self.base_set.union(event_is_download)
        self.event_is_view = self.base_set.union(event_is_view)
        self.event_is_order = self.base_set.union(event_is_order)
        self.event_is_search = self.base_set.union(event_is_search)

    def diff_event(self, method, data):
        data = set(data.keys())
        if method == 'download':
            diff_data1 = self.event_is_download.difference(data)
            diff_data2 = data.difference(self.event_is_download)
        if method == 'view':
            diff_data1 = self.event_is_view.difference(data)
            diff_data2 = data.difference(self.event_is_view)
        if method == 'search':
            diff_data1 = self.event_is_search.difference(data)
            diff_data2 = data.difference(self.event_is_search)
        if method == 'order':
            diff_data1 = self.event_is_order.difference(data)
            diff_data2 = data.difference(self.event_is_order)
        try:
            print(f'xsj相比预期数据少了{diff_data1}')
            print(f'xsj相比预期数据多了{diff_data2}')
            diff_data = diff_data1.union(diff_data2)
            print(f'预期数据与xsj结果数差异{diff_data}')
            return diff_data
        except Exception as e:
            print(f'error------->{e}------->检查传参是否正确')


if __name__ == '__main__':
    diff = DiffExpectVsXsjResult()
    result = diff.diff_event('view', view)
