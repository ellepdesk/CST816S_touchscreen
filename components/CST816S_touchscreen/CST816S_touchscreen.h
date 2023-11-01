#pragma once

#include "esphome/core/component.h"
#include "esphome/components/text_sensor/text_sensor.h"
#include "CST816S.h"

namespace esphome {
namespace cst816s_touchscreen {

class CST816STouchScreen : public text_sensor::TextSensor, public Component {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;
  void set_swap_x_y(bool);
  void set_invert_x(bool);
  void set_invert_y(bool);
};

}  // namespace cst816s_touchscreen
}  // namespace esphome
