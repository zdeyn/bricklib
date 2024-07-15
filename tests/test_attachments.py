# test_attachments.py

import pytest
from bricklib.mixins import AttachmentSocketMixin, AttachmentMixin
from bricklib.types import AttachmentSocket, Attachment

class MySocket(AttachmentSocketMixin):
    """
    Custom socket class inheriting from AttachmentSocketMixin.
    """
    pass

class MyAttachment(AttachmentMixin):
    """
    Custom attachment class inheriting from AttachmentMixin.
    """
    pass

def test_socket_is_attachment_socket():
    """
    Test to ensure MySocket implements the AttachmentSocket protocol.
    """
    socket = MySocket()
    assert isinstance(socket, AttachmentSocket)
    assert socket.attachments == []

def test_attachment_is_attachment():
    """
    Test to ensure MyAttachment implements the Attachment protocol.
    """
    attachment = MyAttachment()
    assert isinstance(attachment, Attachment)
    assert attachment.parent is None

def test_attach():
    """
    Test the attach method of MySocket to ensure it properly attaches a MyAttachment instance.
    """
    socket = MySocket()
    attachment = MyAttachment()

    socket.attach(attachment)
    
    assert attachment in socket.attachments
    assert socket is attachment.parent

def test_attach_rejects_bad_attachment():
    """
    Test the attach method to ensure it raises a TypeError when attaching an invalid object.
    """
    socket = MySocket()
    bad = "not an attachment"

    with pytest.raises(TypeError):
        socket.attach(bad)
    
    assert bad not in socket.attachments

def test_attach_to_rejects_bad_socket():
    """
    Test the _attach_to method to ensure it raises a TypeError when attaching to an invalid object.
    """
    attachment = MyAttachment()
    bad = "not a socket"

    with pytest.raises(TypeError):
        attachment._attach_to(bad)
    
    assert bad is not attachment.parent

if __name__ == "__main__":
    pytest.main()
