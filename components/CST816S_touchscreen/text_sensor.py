import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.const import CONF_ID, CONF_ROTATION

cst816s_touchscreen_ns = cg.esphome_ns.namespace('cst816s_touchscreen')
CST816STouchScreen = cst816s_touchscreen_ns.class_('CST816STouchScreen', text_sensor.TextSensor, cg.Component)

CONF_SWAP_X_Y = "swap_x_y"
CONF_INVERT_X = "invert_x"
CONF_INVERT_Y = "invert_y"


CONFIG_SCHEMA = text_sensor.TEXT_SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(CST816STouchScreen),
    cv.Optional(CONF_SWAP_X_Y): cv.boolean,
    cv.Optional(CONF_INVERT_X): cv.boolean,
    cv.Optional(CONF_INVERT_Y): cv.boolean,
    cv.Optional(CONF_ROTATION): cv.Any([0, 90, 180, 270]),
}).extend(cv.COMPONENT_SCHEMA)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield text_sensor.register_text_sensor(var, config)
    yield cg.register_component(var, config)
    cg.add_library(
            name="CST816S",
            repository="https://github.com/ellepdesk/CST816S.git#add-xy-controls",
            version="1.0.0",
        )

    if CONF_SWAP_X_Y in config:
        cg.add(var.set_swap_x_y(config[CONF_SWAP_X_Y]))
    if CONF_INVERT_X in config:
        cg.add(var.set_invert_x(config[CONF_INVERT_X]))
    if CONF_INVERT_Y in config:
        cg.add(var.set_invert_y(config[CONF_INVERT_Y]))
    if CONF_ROTATION in config:
        degrees = config[CONF_ROTATION]
        if degrees == 00:
            cg.add(var.set_swap_x_y(False))
            cg.add(var.set_invert_x(False))
            cg.add(var.set_invert_x(False))
        if degrees == 90:
            cg.add(var.set_swap_x_y(True))
            cg.add(var.set_invert_x(True))
            cg.add(var.set_invert_x(False))
        elif degrees == 180:
            cg.add(var.set_swap_x_y(False))
            cg.add(var.set_invert_x(True))
            cg.add(var.set_invert_x(True))
        elif degrees == 270:
            cg.add(var.set_swap_x_y(True))
            cg.add(var.set_invert_x(True))
            cg.add(var.set_invert_x(False))


