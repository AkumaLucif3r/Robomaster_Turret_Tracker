# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from interbotix_xs_msgs/MotorGainsRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MotorGainsRequest(genpy.Message):
  _md5sum = "7c362297bf8bae149936ba71305f3900"
  _type = "interbotix_xs_msgs/MotorGainsRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Set PID gains
#
# To get familiar with the various PID gains, go to...
# http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/
# ...click on a motor model, and scroll down to the 'PID' section.

string cmd_type          # set to 'group' if commanding a joint group or 'single' if commanding a single joint
string name              # name of the group if commanding a joint group or joint if commanding a single joint
int32 kp_pos             # acts as a pass-through to the Position_P_Gain register
int32 ki_pos             # acts as a pass-through to the Position_I_Gain register
int32 kd_pos             # acts as a pass-through to the Position_D_Gain register
int32 k1                 # acts as a pass-through to the Feedforward_1st_Gain register
int32 k2                 # acts as a pass-through to the Feedforward_2nd_Gain register
int32 kp_vel             # acts as a pass-through to the Velocity_P_Gain register
int32 ki_vel             # acts as a pass-through to the Velocity_I_Gain register
"""
  __slots__ = ['cmd_type','name','kp_pos','ki_pos','kd_pos','k1','k2','kp_vel','ki_vel']
  _slot_types = ['string','string','int32','int32','int32','int32','int32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       cmd_type,name,kp_pos,ki_pos,kd_pos,k1,k2,kp_vel,ki_vel

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MotorGainsRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.cmd_type is None:
        self.cmd_type = ''
      if self.name is None:
        self.name = ''
      if self.kp_pos is None:
        self.kp_pos = 0
      if self.ki_pos is None:
        self.ki_pos = 0
      if self.kd_pos is None:
        self.kd_pos = 0
      if self.k1 is None:
        self.k1 = 0
      if self.k2 is None:
        self.k2 = 0
      if self.kp_vel is None:
        self.kp_vel = 0
      if self.ki_vel is None:
        self.ki_vel = 0
    else:
      self.cmd_type = ''
      self.name = ''
      self.kp_pos = 0
      self.ki_pos = 0
      self.kd_pos = 0
      self.k1 = 0
      self.k2 = 0
      self.kp_vel = 0
      self.ki_vel = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.cmd_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7i().pack(_x.kp_pos, _x.ki_pos, _x.kd_pos, _x.k1, _x.k2, _x.kp_vel, _x.ki_vel))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.cmd_type = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.cmd_type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.kp_pos, _x.ki_pos, _x.kd_pos, _x.k1, _x.k2, _x.kp_vel, _x.ki_vel,) = _get_struct_7i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.cmd_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7i().pack(_x.kp_pos, _x.ki_pos, _x.kd_pos, _x.k1, _x.k2, _x.kp_vel, _x.ki_vel))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.cmd_type = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.cmd_type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.kp_pos, _x.ki_pos, _x.kd_pos, _x.k1, _x.k2, _x.kp_vel, _x.ki_vel,) = _get_struct_7i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7i = None
def _get_struct_7i():
    global _struct_7i
    if _struct_7i is None:
        _struct_7i = struct.Struct("<7i")
    return _struct_7i
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from interbotix_xs_msgs/MotorGainsResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MotorGainsResponse(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "interbotix_xs_msgs/MotorGainsResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MotorGainsResponse, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
class MotorGains(object):
  _type          = 'interbotix_xs_msgs/MotorGains'
  _md5sum = '7c362297bf8bae149936ba71305f3900'
  _request_class  = MotorGainsRequest
  _response_class = MotorGainsResponse
