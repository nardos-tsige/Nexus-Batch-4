class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i, j = len(players), len(trainers)
        p_ptr, t_ptr = 0, 0
        count = 0
        while p_ptr < i and t_ptr < j:
            if (players[p_ptr] <= trainers[t_ptr]):
                count += 1
                p_ptr += 1
                t_ptr += 1
            else:
                t_ptr += 1
        return count
