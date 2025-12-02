import streamlit as st
from datetime import datetime

st.set_page_config(page_title="To-Do App", page_icon="📝", layout="centered")

# ----- TECH THEME -----
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f0f0f, #1c1c1c);
}
.title {
    font-size: 36px;
    font-weight: 800;
    color: #4ca3dd;
    text-align: center;
    margin-bottom: -5px;
}
.subtitle {
    text-align: center;
    color: #cccccc;
    margin-bottom: 25px;
}
.task-card {
    background: #1e1e1e;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
    border-left: 4px solid #4ca3dd;
}
button {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ----- TITLE -----
st.markdown("<div class='title'>📝 To-Do List</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>A Simple Study Productivity Tool</div>", unsafe_allow_html=True)

# ----- TASK STORAGE -----
if "tasks" not in st.session_state:
    st.session_state.tasks = []


# ----- ADD NEW TASK -----
task = st.text_input("Add a new task:")

if st.button("Add Task ➕"):
    if task.strip():
        st.session_state.tasks.append({"task": task, "done": False, "time": datetime.now().strftime("%H:%M %d-%m-%Y")})
        st.success("Task added!")
    else:
        st.error("Enter a valid task!")


st.write("## Your Tasks:")

# ----- SHOW TASKS -----
if st.session_state.tasks:
    for i, t in enumerate(st.session_state.tasks):

        col1, col2, col3 = st.columns([0.7, 5, 1])

        # Checkbox (DONE/NOT DONE)
        with col1:
            done = st.checkbox("", value=t["done"], key=f"check_{i}")
            st.session_state.tasks[i]["done"] = done

        # Task text
        with col2:
            task_html = f"""
            <div class='task-card'>
                <b style="color:{'#4ca3dd' if not done else '#66cc66'};">
                    {'✔️ ' if done else ''}{t['task']}
                </b><br>
                <span style="color:#888; font-size:12px;">Added: {t['time']}</span>
            </div>
            """
            st.markdown(task_html, unsafe_allow_html=True)

        # DELETE BUTTON
        with col3:
            if st.button("🗑", key=f"del_{i}"):
                st.session_state.tasks.pop(i)
                st.experimental_rerun()

else:
    st.info("No tasks yet. Add one above!")


# ----- CLEAR ALL -----
if st.button("Clear All Tasks ❌"):
    st.session_state.tasks = []
    st.warning("All tasks cleared!")

st.write("---")
st.caption("Made for learning • Streamlit App")
   
    
