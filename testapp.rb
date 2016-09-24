require 'rubygems'
require 'securerandom'
require 'sinatra'
require 'Haml'
require 'active_support/json'
require 'active_support/core_ext/object/json'


get '/' do
  height = params.fetch("h", 1).to_i
  width = params.fetch("w", 1).to_i
  depth = params.fetch("d", 1).to_i
  page_data = generate_page_data(height, width, depth)
  haml :index, locals: {
         page_data: page_data,
         depth: depth,
         width: width,
         height: height,
         link: params[:prev_filename],
       }
end

# Generates data to be converted to json.
#
# {
#   leaves: [
#     { abc: a..z,
#       ... # this is the height
#     },
#     ... # this is the width
#   ],
#   child: {
#     child: .. # this is the depth
#   }
# }
def generate_page_data(height, width, depth)
  value = ('a'..'z').to_a.join('')
  leaf = {}
  height.times do
    leaf[SecureRandom.hex] = value
  end
  root = {}
  current = root
  depth.times do
    leaves = Array.new width, leaf
    node = {leaves: leaves}
    current[:child] = node
    current = node
  end
  root
end
