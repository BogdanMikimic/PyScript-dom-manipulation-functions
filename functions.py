import js
# from functools import partial
# # from pyodide.http import pyfetch
# import asyncio
# import json
# # from pyodide.ffi.wrappers import add_event_listener

# pre-defined DOM manipulation functions
def error_message(message:str="There is an alert, but no text was provided for it") -> None:
    """
    Raises an alert on the HTML page
    :param message: if no message is provided, a standard one is returned
    :return: None
    """
    js.alert(message)

# def get_display_status(tag_object:object) -> str:
#     """
#     Gets the value in the display attribute (in style) of the passed tag object and returns it as string
#     if no status was specifically set, a message is returned
#
#     :param tag_object: An object representing an HTML tag
#     :return: Returns the display status as a string
#     """
#
#     display_status = tag_object.style.display
#     if display_status == '':
#         display_status = "not specified"
#     return display_status
#
# def get_by_id(element_id:str) -> object:
#     # grabs an element from the html by id and returns the element as object
#     my_element = js.document.querySelector(f'#{element_id}')
#     return my_element
#
# def get_by_class(element_class:str, live_list:bool=False) -> list:
#     """Gets all elements from the html with a certain class name.
#     If live_list == True, it used getElementsByClassName which returns a
#     live list, meaning that if one element from the dom that is on that list
#     changes class (on a button push for example), it is dropped from the list. It
#     works the same way if a dom element not in the list is added to that class,
#     it will be added to the live list.
#     If live_list == False is using querySelectorAll, which returns a 'dead list'
#     meaning that the list does not change even if some element from the list
#     changes class, or other elements are added to that class"""
#     if live_list is False:
#         my_list_of_elements = js.document.querySelectorAll(f'.{element_class}')
#         if not my_list_of_elements:
#             return list()
#         else:
#             return my_list_of_elements
#     else:
#         my_list_of_elements = js.document.getElementsByClassName(element_class)
#         if not my_list_of_elements:
#             return list()
#         else:
#             return my_list_of_elements
#
# def set_class(tag_object:object, new_class_name:str) -> None:
#     """Changes the name of the class of the passed object
#     to the new class name provided"""
#     tag_object.className = new_class_name
#
# def get_class(tag_object:object) -> str:
#     """Returns the name of the class of the passed object"""
#     return tag_object.className
#
# def set_id(tag_object:object, my_id:str) -> None:
#     """Sets the id attribute"""
#     tag_object.id = my_id
#
# def prevent_default_action(event=None) -> None:
#     # prevent default action, such as form submit button, navigation, etc
#     js.event.preventDefault()
#
# def set_display_status(tag_object:object, new_display_status:str):
#     # writes a new value of the display attribute (in style)of the tag object passed through
#     # checks that the provided string is a valid value that can be used as a display attribute
#     # if not, the value defaults to "block" and rasise an error - depends on the function error_message
#     display_values = [
#         'none',
#         'block',
#         'inline',
#         'inline-block',
#         'flex',
#         'inline-flex',
#         'grid',
#         'inline-grid',
#         'table',
#         'table-row',
#         'table-cell',
#         'table-caption',
#         'list-item',
#         'run-in',
#         'contents',
#         'flow-root'
#     ]
#     if new_display_status not in display_values:
#         error_message (f'The value "{new_display_status}" that you provided for the display status is not a valid value for the display element. The possible values for the display status are {display_values}. I have changed the display status to "block"')
#         tag_object.style.display = 'block'
#     else:
#         tag_object.style.display = new_display_status
#
# def get_text(tag_object:object) -> str:
#     """Returns the text of the passed object"""
#     return tag_object.textContent
#
# def set_text(tag_object:object, new_text:str):
#     # changes the text of the passed object to the new text provided
#     tag_object.textContent = new_text
#
# def get_value(tag_object:object) -> str:
#     """returns value (text written in) of the passed object - a form field"""
#     return tag_object.value
#
# def set_value(tag_object:object, new_value:str) -> str:
#     """Inserts a value (text written in the field) of the passed object - a form field"""
#     tag_object.value = new_value
#
# def get_title(tag_object:object) -> str:
#     """Returns the title of an object"""
#     return tag_object.title
#
# def play_audio_tag(audio_tag:object) -> None:
#     """Starts playing the content of an <audio> tag"""
#     audio_tag.play()
#
# def listen(tag_object_to_ad_ev_listener_to:object, event_type:str, function_to_be_called_when_event_happens) -> None:
#     """Imports event listener from piodide and takes the tag to add the listener to, the event, and the function to be called"""
#     add_event_listener(tag_object_to_ad_ev_listener_to, event_type, function_to_be_called_when_event_happens)
#
# def get_custom_attribute_value(tag_object:object, attribute_name:str) -> str:
#     """Retrieves the data stored in the custom attribute (data-* of a tag-object)"""
#     return tag_object.getAttribute(attribute_name)
#
# def set_custom_attribute_value(tag_object:object, attribute_name:str, new_attribute_value:str) -> None:
#     """Changes the data stored in the custom attribute (data-* of a tag-object)"""
#     return tag_object.setAttribute(attribute_name, new_attribute_value)
#
# def get_csrf_token_from_cookie(event) -> str:
#     """Extracts the csrftoken from cookies. Requires js module import"""
#     raw_string = js.document.cookie
#     # checks if we have more than one cookie
#     # cookies are returned as a long string like this: "cookie_name1=cookie_value1; cookie_name2=cookie_value2; "
#     if ';' in raw_string:
#         # if we do, it makes them into a list and looks for 'csrftoken'
#         cookies_as_list = raw_string.split('; ')
#         for cookie in cookies_as_list:
#             if cookie.split('=')[0] == 'csrftoken':
#                 return cookie.split('=')[1]
#             else:
#                 js.alert('No csrftoken found in cookies')
#                 return None
#     else:
#         csrftoken = raw_string.split('=')[1]
#         return csrftoken
#
# def remove_required_attr(input_field_obj_to_remove_required_from:object) -> None:
#     input_field_obj_to_remove_required_from.removeAttribute('required')
#
# def create_tag(tag_name:str) -> object:
#     """Creates and returns a tag. If tag does not exist, raises and error"""
#     html_tags = [
#         "!--", "!DOCTYPE", "a", "abbr", "address", "area", "article", "aside", "audio",
#         "b", "base", "bdi", "bdo", "blockquote", "body", "br", "button",
#         "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist",
#         "dd", "del", "details", "dfn", "dialog", "div", "dl", "dt",
#         "em", "embed", "fieldset", "figcaption", "figure", "footer", "form",
#         "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hr", "html",
#         "i", "iframe", "img", "input", "ins", "kbd", "label", "legend",
#         "li", "link", "main", "map", "mark", "meta", "meter", "nav",
#         "noscript", "object", "ol", "optgroup", "option", "output", "p", "param",
#         "picture", "pre", "progress", "q", "rp", "rt", "ruby",
#         "s", "samp", "script", "section", "select", "small", "source", "span",
#         "strong", "style", "sub", "summary", "sup", "svg", "table", "tbody",
#         "td", "template", "textarea", "tfoot", "th", "thead", "time", "title",
#         "tr", "track", "u", "ul", "var", "video", "wbr"
#     ]
#     if tag_name in html_tags:
#         new_tag = js.document.createElement(tag_name)
#         return new_tag
#     else:
#         error_message("There is no tag named like that, I checked!")
#
# def append_child(existing_tag_object:object, new_child_object:object) -> None:
#     """Appends the new tag object as a child of an existing object as it's last child"""
#     existing_tag_object.appendChild(new_child_object)
#
# def add_child_before_existing_tag(parent_tag_object:object, new_child_object:object, existing_child_object) -> None:
#     """Inserts the new tag object as a child of an existing object before an existing child"""
#     parent_tag_object.insertBefore(new_child_object, existing_child_object)
#
# def delete_tag(tag:object) -> None:
#     """Removes a tag object"""
#     tag.remove()
#
# def clone_object_by_id(object_id:object, get_children:bool=True) -> object:
#     """Clones an object (with children if get children is True) and returns it"""
#     parent = get_by_id(object_id)
#     clone = parent.cloneNode(get_children)
#     return clone
#
# def get_first_child_of_object(parent_object:object) -> object:
#     """Returns the child object of a parent object"""
#     return parent_object.firstElementChild
#
# def get_nth_child(parent_object:object, child_number:int) -> object:
#     """Returns the nth child of the object.
#     Children are zero indexed, but I compensate for that"""
#     parent = parent_object
#     child_number_adjusted = child_number - 1
#     nth_child = parent.children[child_number_adjusted]
#     return nth_child
#
# def get_text_of_selected_in_the_drop_down(options_tag_object:object) -> str:
#     """Parses the options on a drop-down 'select' type
#     tag, and returns the text value of the one which is
#     selected (has selected attribute)"""
#     for option in options_tag_object:
#         if option.hasAttribute('selected'):
#             return get_text(option)


error_message('it works')