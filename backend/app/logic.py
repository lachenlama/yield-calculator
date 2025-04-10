class TrancheYield:
    def __init__(self,
                 base_yield,
                 reward_yield,
                 tranche_thickness,
                 base_expected_yield,
                 reward_expected_yield,
                 actual_tranche_yield,
                 actual_tranche_yield_percentage):
        
        self.base_yield = base_yield
        self.reward_yield = reward_yield
        self.tranche_thickness = tranche_thickness
        self.base_expected_yield = base_expected_yield
        self.reward_expected_yield = reward_expected_yield
        self.actual_tranche_yield = actual_tranche_yield
        self.actual_tranche_yield_percentage = actual_tranche_yield_percentage

    def tvl(self):
        return round(self.base_yield + self.reward_yield, 2)
    
    def base_yield_tranche_thickness(self):
        return round(self.base_yield / self.tvl() * 100, 2)
    
    def reward_yield_tranche_thickness(self):
        return round(self.reward_yield / self.tvl() * 100, 2)
    
    def total_expected_yield_percentage(self):
        return round(self.base_expected_yield + self.reward_expected_yield, 2)

    def base_actual_yield(self):
        return round(self.base_expected_yield * self.tvl(), 2)

    def reward_actual_yield(self):
        return round(self.reward_expected_yield * self.tvl(), 2)
    
    def total_actual_yield(self):
        return round(self.base_actual_yield() + self.reward_actual_yield(), 2)
    
    def base_actual_tranche_yield(self):
        return round((self.base_actual_yield() / self.base_yield) * 100, 2)
    
    def reward_actual_tranche_yield(self):
        return round((self.reward_actual_yield() / self.reward_yield) * 100, 2)
    
    def total_actual_tranche_yield(self):
        return round(self.total_actual_yield() / self.tvl() * 100, 2)

    @staticmethod
    def test_csv_examples():
        """Test against CSV example values"""
        # Main example
        ty1 = TrancheYield(
            base_yield=100000,
            reward_yield=4000,
            tranche_thickness=None,
            base_expected_yield=0.12,
            reward_expected_yield=0.15,
            actual_tranche_yield=None,
            actual_tranche_yield_percentage=None
        )
        
        print("\nTesting Main CSV Example:")
        print(f"TVL: {ty1.tvl()} (Expected: 104000)")
        print(f"Base Tranche %: {ty1.base_yield_tranche_thickness()}% (Expected: 96.15%)")
        print(f"Reward Tranche %: {ty1.reward_yield_tranche_thickness()}% (Expected: 3.85%)")
        print(f"Base Actual Yield: {ty1.base_actual_yield()} (Expected: 12480)")
        print(f"Reward Actual Yield: {ty1.reward_actual_yield()} (Expected: 600)")
        print(f"Total Actual Yield: {ty1.total_actual_yield()} (Expected: 13080)")
        print(f"Base Actual Tranche Yield: {ty1.base_actual_tranche_yield()} (Expected: 0.1248)")
        print(f"Reward Actual Tranche Yield: {ty1.reward_actual_tranche_yield()} (Expected: 0.15)")
        print(f"Total Actual Tranche Yield: {ty1.total_actual_tranche_yield()} (Expected: 0.1258)")
