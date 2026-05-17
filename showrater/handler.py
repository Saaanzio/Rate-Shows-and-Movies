import streamlit as st
import pandas as pd

from show.show_service import ShowService

show_service = ShowService()
PAGE_SIZE = 5

def render() -> None:
    header()
    filters()
    table()


def header() -> None:
    title, line = st.columns([8, 7], vertical_alignment="center", gap=None)

    with title:
        st.title("🍿 Stream Track")
    with line:
        st.markdown("<hr>", unsafe_allow_html=True)


def filters() -> None:
    search, order, update, create = st.columns([3.5,2,2,2], vertical_alignment="center")
    with search:
        search = st.text_input(label="", value="", label_visibility="collapsed", icon="🔎")
        st.session_state["search_name"] = search
    with order:
        order_filters = st.selectbox(label="", options=["None", "Desc", "Asc"], placeholder="Order by", label_visibility="collapsed")
        st.session_state["search_order"] = order_filters
    with update:
        if st.button("Update", icon="🔃", width="stretch"):
            st.rerun()
    with create:
        if st.button("Create", icon="➕", width="stretch"):
            create_modal()


@st.dialog("Rate a show")
def create_modal() -> None:
    name = st.text_input("Name*")
    review = st.text_area("Review")
    rating = st.slider("Rating*", min_value=1, max_value=5, value = 3)

    _, cancel, create = st.columns([9,2.5,2.5], gap="xsmall")

    with create:
        save_clicked = st.button("Save", width="stretch")
    with cancel:
        if st.button("Cancel", width="stretch"):
            st.rerun()

    if save_clicked:
        if not name:
            st.error("Please fill the name")
        else:
            show_service.save_review(name, review, rating)
            st.rerun()


def table():
    search = st.session_state.get("search_name", "")
    order = st.session_state.get("search_order")

    data = show_service.get_all_reviews()

    if search:
        data = [
            row for row in data
                if search.lower() in row["name"].lower()
        ]

    if order == "Asc":
        data = sorted(data, key=lambda row: row["rating"])
    elif order == "Desc":
        data = sorted(data, key=lambda row: row["rating"], reverse=True)

    st.divider()
    name_header, review_header, rating_header, action_header = st.columns(4, vertical_alignment="center", border=True)

    with name_header:
        st.write("Name")
    with review_header:
        st.write("Review")
    with rating_header:
        st.write("Rating")
    with action_header:
        st.write("Action")

    for row in data:
        name, review, rating, action_btn = st.columns(4, vertical_alignment="center")

        with name:
            st.write(row["name"])
        with review:
            st.write(row["description"] or "Sem review")
        with rating:
            st.write(str(row["rating"]) + "⭐")
        with action_btn:
            edit, delete = st.columns(2, gap="xsmall")
            with edit:
                if st.button("", icon="✏️", key=f"edit_{row["id"]}", width="stretch"):
                    edit_modal(row["id"])
            with delete:
                if st.button("", icon="🗑️", key=f"delete_{row["id"]}", width="stretch"):
                    delete_modal(row["id"])


@st.dialog("✏️ Edit review")
def edit_modal(item_id) -> None:
    item = show_service.get_review_by_id(item_id)

    name = st.text_input(label="Nome*", value=item[1])
    review = st.text_area(label="Review", value=item[2] or "")
    rating = st.slider(label="Rating*", min_value=1, max_value=5, value=item[3])

    _, cancel, save = st.columns([9, 2.5, 2.5], gap="xsmall")

    with save:
        save_clicked = st.button("Save", width="stretch")
    with cancel:
        if st.button("Cancel", width="stretch"):
            st.rerun()

    if save_clicked:
        if not name:
            st.error("Please fill the name")
        else:
            show_service.update_review(item[0], name, review, rating)
            st.rerun()


@st.dialog("🗑️ Delete a review")
def delete_modal(item_id: int) -> None:
    st.warning("⚠️ This action is irreversible")

    _, cancel, delete = st.columns([9, 3,3], gap="xsmall")
    with delete:
        if st.button("Delete", width="stretch"):
            show_service.delete_review(item_id)
            st.rerun()
    with cancel:
        if st.button("Cancel", width="stretch"):
            st.rerun()


if __name__ == "__main__":
    render()

