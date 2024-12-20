// ///////////////////////
// //                   //
// //  File Attributes  //
// //                   //
// ///////////////////////

// Filename: bg.bmp
// Pixel Width: 160px
// Pixel Height: 144px

// /////////////////
// //             //
// //  Constants  //
// //             //
// /////////////////

const int bg_tile_map_size = 0x021C;
const int bg_tile_map_width = 0x1E;
const int bg_tile_map_height = 0x12;

const int bg_tile_data_size = 0x0710;
const int bg_tile_count = 0x71;

// ////////////////
// //            //
// //  Map Data  //
// //            //
// ////////////////

const unsigned char bg_map_data[] ={
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x01,0x02,0x03,0x04,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x05,0x06,
  0x07,0x08,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x09,0x0A,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x0B,0x0C,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x0D,0x0E,0x0F,0x10,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x11,0x12,0x13,0x14,0x15,0x00,0x00,0x16,0x17,0x18,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x19,0x1A,0x1B,0x1C,0x1D,0x1E,0x1F,0x20,0x21,0x22,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x23,0x24,0x25,0x26,0x27,0x28,0x29,0x2A,0x2B,0x2C,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x2D,0x2E,0x2F,0x30,0x31,0x00,0x00,0x05,0x32,0x33,0x34,0x35,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x36,0x37,
  0x38,0x08,0x00,0x00,0x00,0x00,0x00,0x39,0x3A,0x3B,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x3C,0x3D,0x00,
  0x00,0x00,0x00,0x00,0x00,0x3E,0x3F,0x40,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x41,0x42,0x43,0x44,0x00,0x00,
  0x00,0x00,0x00,0x45,0x34,0x46,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x47,0x48,0x49,0x4A,0x4B,0x4C,0x4D,0x00,0x00,0x4E,
  0x4F,0x50,0x3A,0x3B,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x51,0x52,0x53,0x54,0x55,0x56,0x57,0x58,0x1E,0x59,0x5A,0x5B,
  0x5C,0x5D,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x5E,0x5F,0x60,0x61,0x62,0x63,0x64,0x28,0x28,0x65,0x66,0x67,0x68,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x69,0x6A,0x6B,0x6C,0x6D,0x6E,0x00,0x00,0x6F,0x70,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
};

// /////////////////
// //             //
// //  Tile Data  //
// //             //
// /////////////////

const unsigned char bg_tile_data[] ={
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x00,0x00,0x07,0x07,0x07,0x07,0x05,0x07,0x05,0x07,0x03,0x03,0x03,0x03,0x01,0x01,
  0x00,0x00,0xF0,0xFF,0x1C,0xE0,0x07,0xF8,0x00,0xFF,0xF0,0xFF,0xFF,0xFF,0xBF,0xFF,
  0x00,0x00,0x0F,0xFF,0x38,0x07,0xE0,0x1F,0x00,0xFF,0x0F,0xFF,0xFF,0xFF,0xFD,0xFF,
  0x00,0x00,0xE0,0xE0,0xE0,0xE0,0xA0,0xE0,0x80,0xC0,0xC0,0xC0,0x80,0x80,0x80,0x80,
  0x01,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0xFE,0xFF,0x3C,0x3F,0x38,0x3F,0x28,0x3F,0x28,0x3F,0x08,0x1F,0x08,0x1F,0x08,0x1F,
  0x7F,0xFF,0x3C,0xFC,0x1C,0xFC,0x14,0xFC,0x14,0xFC,0x10,0xF8,0x10,0xF8,0x10,0xF8,
  0x80,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x08,0x1F,0x08,0x1F,0x08,0x1F,0x08,0x1F,0x08,0x1F,0x08,0x1F,0x08,0x1F,0x08,0x1F,
  0x10,0xF8,0x10,0xF8,0x10,0xF8,0x10,0xF8,0x10,0xF8,0x10,0xF8,0x10,0xF8,0x10,0xF8,
  0x08,0x1F,0x08,0x1F,0x08,0x1F,0x09,0x1E,0x00,0x1F,0x09,0x1E,0x00,0x1F,0x01,0x1E,
  0x10,0xF8,0x10,0xF8,0x10,0xF8,0x00,0xF8,0x10,0xF8,0x00,0xF8,0x90,0x78,0x80,0x78,
  0x00,0x00,0x00,0x00,0x00,0x00,0x04,0x07,0x05,0x07,0x05,0x07,0x07,0x07,0x07,0x07,
  0x01,0x1E,0x43,0x9C,0x9C,0xDF,0x18,0xE0,0x07,0xF8,0x00,0xFF,0xF0,0xFF,0x1C,0xE0,
  0x80,0x78,0xC2,0x39,0x39,0xFB,0x18,0x07,0xE0,0x1F,0x00,0xFF,0x0F,0xFF,0x38,0x07,
  0x00,0x00,0x00,0x00,0x00,0x00,0x20,0xE0,0xA0,0xE0,0xA0,0xE0,0xE0,0xE0,0xE0,0xE0,
  0x05,0x07,0x05,0x07,0x07,0x07,0x03,0x03,0x01,0x01,0x01,0x01,0x00,0x00,0x00,0x00,
  0x07,0xF8,0x00,0xFF,0xF0,0xFF,0xFF,0xFF,0xBF,0xFF,0xFE,0xFF,0x3C,0x3F,0x38,0x3F,
  0xE0,0x1F,0x00,0xFF,0x0F,0xFF,0xFF,0xFF,0xFD,0xFF,0x7F,0xFF,0x3F,0xFF,0x1F,0xFF,
  0xA0,0xE0,0xA0,0xE0,0xE0,0xE0,0xC0,0xC0,0x8C,0x8C,0x81,0x8F,0xF1,0xFF,0xE1,0xDF,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x10,0xF0,0x1C,0xFC,0x0C,0xF4,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x01,0x07,0x07,0x06,0x05,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x10,0xFE,0x01,0xFF,0x00,0xFF,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xC0,0xC0,0xC0,0x40,
  0x28,0x3F,0x28,0x3F,0x28,0x3F,0x28,0x3F,0x28,0x3F,0x28,0x3F,0x28,0x3F,0x28,0x3F,
  0x0F,0xFF,0x01,0xFF,0x00,0xFF,0x2F,0xD0,0x7F,0x80,0xFA,0x05,0x50,0xAF,0x80,0x7F,
  0xDE,0xF1,0xFE,0xF1,0x60,0x91,0xC1,0x10,0x05,0x10,0xEF,0x10,0x11,0xFE,0x10,0xFF,
  0xF4,0x1C,0xFF,0x1F,0x4C,0x13,0x07,0x10,0x20,0x10,0xEF,0x10,0x10,0xFF,0x10,0xFF,
  0x00,0x00,0xFF,0xFF,0x00,0xFF,0xFF,0x00,0xBF,0x00,0xFF,0x00,0x00,0xFF,0x00,0xFF,
  0x00,0x00,0xFF,0xFF,0x00,0xFF,0xFF,0x00,0xFF,0x00,0xFF,0x00,0x00,0xFF,0x00,0xFF,
  0x05,0x07,0xFF,0xFF,0x06,0xF9,0xFC,0x01,0xF8,0x01,0xFE,0x01,0x01,0xFF,0x01,0xFF,
  0xEF,0x11,0xFF,0x01,0x14,0x01,0x10,0x01,0x52,0x01,0xEE,0x11,0x01,0xFF,0x01,0xFF,
  0x40,0xC0,0xC0,0xC0,0xC1,0x3F,0x78,0x07,0x1E,0x01,0xFF,0x00,0x07,0xF8,0x01,0xFE,
  0x00,0x00,0x00,0x00,0x80,0x80,0x60,0xE0,0x10,0xF0,0x00,0xF0,0x84,0x7C,0xC4,0x3C,
  0x28,0x3F,0x28,0x3F,0x28,0x3F,0x29,0x3E,0x20,0x3F,0x29,0x3E,0x20,0x3F,0x21,0x3E,
  0x41,0xBF,0x83,0x7F,0x06,0xFF,0x85,0x7F,0x0B,0xFF,0x87,0x7F,0x97,0x7F,0x87,0x7F,
  0xF0,0xFF,0xF0,0xFF,0x7F,0xFF,0xFF,0xFF,0xFF,0xFF,0xD1,0xFF,0xD1,0xFF,0xFF,0xFF,
  0x1F,0xFF,0x1F,0xFF,0xFE,0xFF,0xFF,0xFF,0xFF,0xFF,0x14,0xFC,0x14,0xFC,0xFC,0xFC,
  0xFF,0xFF,0xFF,0xFF,0x80,0xFF,0xFF,0xFF,0xFF,0xFF,0x00,0x00,0x00,0x00,0x00,0x00,
  0xFF,0xFF,0xFF,0xFF,0x00,0xFF,0xFF,0xFF,0xFF,0xFF,0x00,0x00,0x00,0x00,0x00,0x00,
  0xFF,0xFF,0xFF,0xFF,0x07,0xFF,0xFF,0xFF,0xFF,0xFF,0x01,0x03,0x01,0x03,0x03,0x03,
  0x11,0xFF,0x11,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0x11,0xFF,0x11,0xFF,0xFF,0xFF,
  0xF0,0xFF,0xF8,0xFF,0xEC,0xFF,0xF4,0xFF,0xF8,0xFF,0x7C,0xFF,0x7C,0xFF,0xFC,0xFF,
  0xE0,0x1C,0x43,0xBF,0x21,0xDF,0x11,0xEF,0x21,0xDF,0x30,0xCF,0x30,0xCF,0x30,0xCF,
  0x01,0x01,0x01,0x01,0x03,0x03,0x04,0x07,0x05,0x07,0x05,0x07,0x04,0x07,0x04,0x07,
  0xE1,0xFE,0x63,0xBC,0xBC,0xFF,0x18,0xE0,0x07,0xF8,0x00,0xFF,0x1F,0xE0,0x00,0xFF,
  0x87,0x7F,0xC6,0x3D,0x3D,0xFF,0x18,0x07,0xE0,0x1F,0x00,0xFF,0x82,0x7F,0x02,0xFF,
  0x9F,0x9F,0x8F,0x8F,0x80,0x80,0x20,0xE0,0xA0,0xE0,0xA0,0xE0,0x80,0x80,0x80,0x80,
  0xF0,0xF0,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0xFE,0xFE,0x3E,0x3E,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x3C,0x3F,0x2C,0x37,0x37,0x3F,0x83,0xFC,0xA0,0xFF,0xA0,0xFF,0xFE,0xFF,0xE3,0xFC,
  0x30,0xCF,0x78,0x87,0x87,0xFF,0x03,0x00,0xFC,0x03,0x00,0xFF,0x01,0xFF,0x87,0x00,
  0x00,0x00,0xD0,0xB0,0xB0,0xF0,0x00,0xF8,0x10,0xF8,0x10,0xF8,0xF8,0xF8,0x18,0xF8,
  0x07,0x07,0x07,0x07,0x06,0x07,0x07,0x07,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0xC0,0xFF,0xFF,0xFF,0xFF,0xFF,0xF9,0xFF,0xF0,0xFF,0xE0,0xFF,0xA0,0xFF,0xA0,0xFF,
  0x3F,0xFF,0xFF,0xFF,0xF6,0xFE,0xFE,0xFE,0xF0,0xF0,0x70,0xF0,0x50,0xF0,0x50,0xF0,
  0xA0,0xFF,0xA0,0xFF,0x7E,0x7F,0x7F,0x7F,0x37,0x3F,0x3F,0x3F,0x07,0x07,0x07,0x07,
  0xFC,0x03,0x00,0xFF,0x01,0xFF,0xFF,0xFF,0xFF,0xFF,0xCF,0xFF,0x87,0xFF,0x03,0xFF,
  0x10,0xF8,0x10,0xF8,0xF8,0xF8,0xF0,0xF0,0xB0,0xF0,0xF0,0xF0,0x80,0x80,0x80,0x80,
  0xA0,0xFF,0xA0,0xFF,0xA0,0xFF,0xA4,0xFB,0x80,0xFF,0xA4,0xFB,0x82,0xFD,0x86,0xF9,
  0x50,0xF0,0x50,0xF0,0x50,0xF0,0x10,0xF0,0x50,0xF0,0x10,0xF0,0x50,0xF0,0x10,0xF0,
  0x05,0x07,0x05,0x07,0x05,0x07,0x05,0x07,0x04,0x07,0x05,0x07,0x04,0x07,0x04,0x07,
  0x02,0xFF,0x02,0xFF,0x02,0xFF,0x20,0xDF,0x02,0xFF,0x20,0xDF,0x12,0xEF,0x30,0xCF,
  0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,
  0x07,0x07,0x05,0x06,0x0E,0x0F,0x00,0x0F,0x14,0x1F,0x14,0x1F,0x1F,0x1F,0x1C,0x1F,
  0x86,0xF9,0x8F,0xF0,0xF0,0xFF,0x60,0x80,0x1F,0xE0,0x00,0xFF,0xC0,0xFF,0x70,0x80,
  0x18,0xF8,0x1A,0xF6,0xF7,0xFF,0x60,0x1F,0x82,0x7F,0x02,0xFF,0x3F,0xFF,0xE3,0x1F,
  0x00,0x00,0x00,0x00,0x00,0x00,0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,
  0x3C,0x3F,0x2C,0x37,0x37,0x3F,0x03,0x7C,0xA0,0xFF,0xA0,0xFF,0xFE,0xFF,0xE3,0xFC,
  0xF0,0xF0,0xD0,0xB0,0xB0,0xF0,0x00,0xF8,0x10,0xF8,0x10,0xF8,0xF8,0xF8,0x18,0xF8,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x01,0x01,0x01,0x01,0x01,
  0x00,0x00,0x00,0x00,0x00,0x00,0x0C,0x0C,0x47,0x7F,0xC2,0xFF,0x82,0x7F,0x78,0xC7,
  0x14,0x1F,0x14,0x1F,0x1F,0x1F,0x0F,0x0F,0xC6,0xC7,0x27,0xE7,0x20,0xE0,0x18,0xE8,
  0x1F,0xE0,0x00,0xFF,0xC0,0xFF,0xFF,0xFF,0xFF,0xFF,0xF9,0xFF,0xF0,0xFF,0xE0,0xFF,
  0x82,0x7F,0x02,0xFF,0x3F,0xFF,0xFF,0xFF,0xF6,0xFE,0xFE,0xFE,0xFF,0xFF,0x7F,0xFF,
  0x80,0x80,0x80,0x80,0x80,0x80,0x00,0x00,0x3F,0x3F,0x06,0x3F,0xC2,0xFF,0x80,0x7F,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xC0,0xC0,0x20,0xE0,0x38,0xF8,0x18,0xE8,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x02,0x03,0x0E,0x0F,0x0C,0x0B,
  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x7E,0x7E,0x31,0xFF,0x11,0xFF,0x00,0xFF,
  0xA0,0xFF,0xA0,0xFF,0x7E,0x7F,0x7F,0x7F,0x37,0x3F,0x3F,0x3F,0xFF,0xFF,0xFF,0x7F,
  0xFF,0xFF,0x01,0xFE,0xFF,0x00,0xFE,0x00,0xFF,0x00,0x00,0xFF,0x00,0xFF,0xFF,0xFF,
  0xFD,0xC2,0x85,0x42,0x06,0x40,0x16,0x40,0xBA,0x44,0x41,0xFE,0x40,0xFF,0xC4,0xFF,
  0xE9,0x39,0xFE,0x3F,0x98,0x27,0x0F,0x20,0x43,0x20,0xDA,0x25,0x20,0xFF,0x20,0xFF,
  0xC0,0xFF,0x00,0xFF,0x17,0xE8,0xFB,0x00,0xD1,0x00,0xFB,0x00,0x5F,0xA0,0x0A,0xF5,
  0x3F,0xFF,0x07,0xFF,0x41,0xBE,0xFF,0x00,0x7C,0x00,0xEB,0x14,0x40,0xBF,0x00,0xFF,
  0x79,0xC6,0xFD,0xC2,0x86,0x40,0x06,0x40,0x16,0x40,0xB9,0x46,0x40,0xFF,0x40,0xFF,
  0xE8,0x38,0xFF,0x3F,0x98,0x27,0x0F,0x20,0x41,0x20,0xDF,0x20,0x20,0xFF,0x20,0xFF,
  0x00,0x00,0xFF,0xFF,0x00,0xFF,0xFF,0x00,0x7F,0x00,0xFF,0x00,0x00,0xFF,0x00,0xFF,
  0x0B,0x0E,0xFF,0xFE,0x0C,0xF2,0xF8,0x02,0xF0,0x02,0xFD,0x02,0x02,0xFF,0x02,0xFF,
  0xCF,0x31,0xEF,0x11,0x34,0x01,0x30,0x01,0xB2,0x01,0xCE,0x31,0x01,0xFF,0x01,0xFF,
  0x7E,0xFF,0xF0,0xFF,0xC0,0x3F,0x7F,0x00,0x1E,0x01,0xE0,0x1F,0x00,0xFF,0x03,0xFF,
  0x02,0xFF,0x02,0xFF,0x85,0x7F,0x05,0xFF,0x0B,0xFF,0x12,0xFE,0x66,0xFE,0xCC,0xFC,
  0x80,0x80,0x80,0x80,0x80,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0xFF,0xFF,0x01,0xFF,0xFF,0xFF,0xFF,0xFF,0x01,0x01,0x01,0x01,0x01,0x01,0x00,0x00,
  0xC4,0xFF,0xFE,0xFF,0xFF,0xFF,0xFF,0xFF,0x47,0xFF,0x46,0xFF,0xFE,0xFF,0x3F,0x3F,
  0x3E,0xFF,0x3F,0xFF,0xFD,0xFF,0xFE,0xFF,0xE3,0xE3,0x23,0xE3,0x20,0xE0,0xE0,0xE0,
  0x05,0xFA,0x0A,0xF5,0x84,0xFB,0x82,0xFD,0x04,0xFB,0x86,0xF9,0x86,0xF9,0x86,0xF9,
  0x07,0xFF,0x0F,0xFF,0x19,0xFF,0x17,0xFF,0x2F,0xFF,0x1F,0xFF,0x50,0xF0,0x10,0xF0,
  0xC4,0xFF,0xC6,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0x46,0xFF,0x46,0xFF,0xFF,0xFF,
  0x3F,0xFF,0x3F,0xFF,0xFD,0xFF,0xFF,0xFF,0xFF,0xFF,0x28,0xF8,0x28,0xF8,0xF8,0xF8,
  0xFE,0xFF,0xFE,0xFF,0x0F,0xFF,0xFF,0xFF,0xFF,0xFF,0x0A,0x0F,0x0A,0x0F,0x0F,0x0F,
  0x21,0xFF,0x31,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0x31,0xFF,0x31,0xFF,0xFF,0xFF,
  0xFF,0xFF,0xFE,0xFF,0xFB,0xFF,0xFF,0xFF,0xFE,0xFE,0x40,0xC0,0x40,0xC0,0xC0,0xC0,
  0x38,0xF8,0xF0,0xF0,0xE0,0xE0,0x80,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x3F,0x3F,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0xE3,0xE3,0x01,0x02,0x0E,0x0F,0x10,0x1F,0x14,0x1F,0x14,0x1F,0x1F,0x1F,0x00,0x00,
  0x86,0xF9,0x8F,0xF0,0xF0,0xFF,0x60,0x80,0x1F,0xE0,0x00,0xFF,0xC0,0xFF,0x00,0x00,
  0x18,0xF8,0x18,0xF4,0xF7,0xFF,0x60,0x1F,0x82,0x7F,0x02,0xFF,0x3F,0xFF,0x00,0x00,
  0xFF,0xFF,0x7F,0x7F,0x00,0x00,0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x80,0x00,0x00,
  0xC0,0xC0,0xC0,0xC0,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0x01,0x01,0x01,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
  0xFF,0xFF,0xFE,0xFE,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
};
