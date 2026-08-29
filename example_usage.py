from client import RolePlayingAutonomousAgentCrewOrchestratorClient

def main():
    client = RolePlayingAutonomousAgentCrewOrchestratorClient()
    res = client.execute_crew_mission('Perform end-to-end security penetration test and generate compliance remediation report')
    print('Crew Mission: ' + res['crew_mission_id'] + ' (' + str(res['agents_active_count']) + ' agents active)')
    print('Tasks Executed: ' + str(res['tasks_executed_hierarchically']) + ' | Delegations: ' + str(res['inter_agent_delegations_completed']))
    print('Success: ' + str(res['mission_success_rate_pct']) + '%')
    print('Deliverables: ' + res['compiled_deliverables_url'])

if __name__ == '__main__':
    main()
