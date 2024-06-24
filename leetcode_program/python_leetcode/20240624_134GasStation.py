class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank,current_tank = 0,0
        # total_tankとcurrent_tankを0に初期化します。
        # total_tankは全体のガスの収支を追跡し、
        # current_tankは現在のセグメントのガスの収支を追跡します。
        total_tank, current_tank = 0, 0
        # starting_stationは仮の出発ガソリンスタンドのインデックスを記憶します。初期値は0です。
        starting_station = 0
        # ガソリンスタンドの数だけループします。
        for i in range(len(gas)):
            # gas[i] - cost[i]をtotal_tankに加算します。
            # これにより、全体のガスの収支が計算されます。
            total_tank += gas[i] - cost[i]
            # gas[i] - cost[i]をcurrent_tankに加算します。
            # これにより、現在のセグメントのガスの収支が計算されます。
            current_tank += gas[i] - cost[i]
            # current_tankが負になった場合、
            # 現在のstarting_stationから出発して一周することが不可能であることを意味します。
            if current_tank < 0:
                # 新しい出発地点を次のガソリンスタンド（i + 1）に設定します。
                starting_station = i + 1
                # current_tankを0にリセットします。
                current_tank = 0
        # 全てのガソリンスタンドをループした後、
        # total_tankが非負（0以上）であれば、出発地点から一周できることを意味します。
        # その場合、starting_stationを返します。
        return starting_station if total_tank >= 0 else -1