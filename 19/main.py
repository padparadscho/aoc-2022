import re


with open('19/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def parse_blueprint(line):
    nums = list(map(int, re.findall(r'\d+', line)))
    return {
        'id': nums[0],
        'ore_cost': nums[1],
        'clay_cost': nums[2],
        'obs_ore_cost': nums[3],
        'obs_clay_cost': nums[4],
        'geode_ore_cost': nums[5],
        'geode_obs_cost': nums[6]
    }


def max_geodes(bp, time_limit):
    # Maximum useful robots: no need to build more than max cost for each resource
    max_ore = max(bp['ore_cost'], bp['clay_cost'], bp['obs_ore_cost'], bp['geode_ore_cost'])
    max_clay = bp['obs_clay_cost']
    max_obs = bp['geode_obs_cost']
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dfs(t, ore, clay, obs, ore_r, clay_r, obs_r, geode_r):
        if t == 0:
            return 0
        
        # Cap resources at what we can spend (prunes state space)
        ore_n = min(ore + ore_r, t * max_ore)
        clay_n = min(clay + clay_r, t * max_clay)
        obs_n = min(obs + obs_r, t * max_obs)
        
        best = 0
        
        # Build geode robot (always optimal if possible)
        if ore >= bp['geode_ore_cost'] and obs >= bp['geode_obs_cost']:
            return dfs(t - 1, ore_n - bp['geode_ore_cost'], clay_n, obs_n - bp['geode_obs_cost'], ore_r, clay_r, obs_r, geode_r + 1) + geode_r
        
        # Build obsidian robot
        if ore >= bp['obs_ore_cost'] and clay >= bp['obs_clay_cost'] and obs_r < max_obs:
            best = max(best, dfs(t - 1, ore_n - bp['obs_ore_cost'], clay_n - bp['obs_clay_cost'], obs_n, ore_r, clay_r, obs_r + 1, geode_r))
        
        # Build clay robot
        if ore >= bp['clay_cost'] and clay_r < max_clay:
            best = max(best, dfs(t - 1, ore_n - bp['clay_cost'], clay_n, obs_n, ore_r, clay_r + 1, obs_r, geode_r))
        
        # Build ore robot
        if ore >= bp['ore_cost'] and ore_r < max_ore:
            best = max(best, dfs(t - 1, ore_n - bp['ore_cost'], clay_n, obs_n, ore_r + 1, clay_r, obs_r, geode_r))
        
        # Wait
        best = max(best, dfs(t - 1, ore_n, clay_n, obs_n, ore_r, clay_r, obs_r, geode_r))
        
        return best + geode_r
    
    return dfs(time_limit, 0, 0, 0, 1, 0, 0, 0)


def solve_part_1(lines):
    blueprints = [parse_blueprint(line) for line in lines]
    total = sum(bp['id'] * max_geodes(bp, 24) for bp in blueprints)

    print(f"Part 1 Solution: {total}")


def solve_part_2(lines):
    blueprints = [parse_blueprint(line) for line in lines[:3]]
    total = 1
    for bp in blueprints:
        total *= max_geodes(bp, 32)
    
    print(f"Part 2 Solution: {total}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)