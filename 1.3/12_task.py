def MassVote(N, Votes):
    summ_Votes = sum(Votes)
    max_val_Votes = max(Votes)
    max_count = Votes.count(max_val_Votes)
    winner_index = next(i for i in range(N) if Votes[i] == max_val_Votes) + 1
    
    return (
        "no winner" if max_count > 1 else
        "minority winner 1" if N == 1 and summ_Votes == 0 else
        f"minority winner {winner_index}" if max_val_Votes * 100 <= summ_Votes * 50 else
        f"majority winner {winner_index}" 
    )