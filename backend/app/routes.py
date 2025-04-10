from flask import Blueprint, request, jsonify, send_from_directory
from .logic import TrancheYield
import os

routes = Blueprint('TrancheYieldCalculator', __name__)

@routes.route('/')
def index():
    return send_from_directory(os.path.join('..', 'static'), 'index.html')

@routes.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join('..', 'static'), filename)

@routes.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    ty = TrancheYield(
        base_yield=data['base_yield'],
        reward_yield=data['reward_yield'],
        tranche_thickness=None,
        base_expected_yield=data['base_expected_yield'],
        reward_expected_yield=data['reward_expected_yield'],
        actual_tranche_yield=None,
        actual_tranche_yield_percentage=None
    )
    
    return jsonify({
        'tvl': ty.tvl(),
        'base_tranche_percent': ty.base_yield_tranche_thickness(),
        'reward_tranche_percent': ty.reward_yield_tranche_thickness(),
        'total_expected_yield_percentage': ty.total_expected_yield_percentage(), 
        'base_actual_yield': ty.base_actual_yield(),
        'reward_actual_yield': ty.reward_actual_yield(),
        'total_actual_yield': ty.total_actual_yield(),
        'base_actual_tranche_yield': ty.base_actual_tranche_yield(),
        'reward_actual_tranche_yield': ty.reward_actual_tranche_yield(),
        'total_actual_tranche_yield': ty.total_actual_tranche_yield()
    })
