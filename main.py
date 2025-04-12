from ai_planner import get_plan_from_ai
from command_executor import execute_plan
from feedback_handler import handle_feedback

def main():
    print("🤖 Welcome to AI Agent!")
    task = input("📝 What task should I perform? ")

    plan = get_plan_from_ai(task)
    print("\n📋 AI-generated plan:")
    print(plan)

    confirm = input("\nDo you approve this plan? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("❌ Task cancelled.")
        return

    success = execute_plan(plan)

    while not success:
        reason = input("❌ Task failed. Can you describe what went wrong? ")
        plan = handle_feedback(task, plan, reason)
        print("\n🔁 Updated plan:")
        print(plan)
        confirm = input("\nDo you want to try again? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("🚪 Exiting...")
            return
        success = execute_plan(plan)

    print("✅ Task completed successfully!")

if __name__ == "__main__":
    main()
