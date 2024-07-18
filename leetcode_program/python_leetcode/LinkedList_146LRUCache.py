from collections import OrderedDict

class LRUCache:
    # 初期化メソッド。LRUキャッシュの容量を設定し、キャッシュをOrderedDictで初期化する
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    # 指定されたキーの値を取得するメソッド。キーが存在しない場合は-1を返す
    def get(self, key: int) -> int:
        # キーがキャッシュに存在しない場合
        if key not in self.cache:
            return -1
        else:
            # キーがキャッシュに存在する場合、キーを最も最近使われた位置に移動
            self.cache.move_to_end(key)
            # キーの値を返す
            return self.cache[key]
    # 指定されたキーと値をキャッシュに追加するメソッド。容量を超えた場合は最も古いキーを削除する
    def put(self, key: int, value: int) -> None:
        # キーが既に存在する場合
        if key in self.cache:
            # キーを最も最近使われた位置に移動
            self.cache.move_to_end(key)
        # キーと値をキャッシュに追加または更新
        self.cache[key] = value
        # キャッシュの容量が超えた場合
        if len(self.cache) > self.capacity:
            # 最初の要素を削除
            self.cache.popitem(last=False)
# Your LRUCache object will be instantiated and called as such:
# LRUCacheオブジェクトを容量を指定して初期化する
# obj = LRUCache(capacity)
# 指定されたキーの値を取得する
# param_1 = obj.get(key)
# 指定されたキーと値をキャッシュに追加または更新する
# obj.put(key, value)
