import * as constatns from "../constants/action-types"
import { fetch as fetchPolyfill } from 'whatwg-fetch'

export function fetchBoardState(url, payload={}){
  return dispatch => {
    dispatch(playerTurn(false));

    fetchPolyfill(url, {
      method:'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body:JSON.stringify(payload)
    })
    .then((response) => {
      if (!response.ok) throw Error(response.statusText);
      else return response;
    })
    .then((response) => response.json())
    .then((data) => normalizeData(data))
    .then((data) => dispatch(stateFetchSuccess(data)))
    .then(() => dispatch(playerTurn(true)))
    .catch((e) => {
      console.log(e);
      return dispatch(stateHasError(true));
    });
  }
}

function normalizeData(data){
  let statePart = {fields:{}, pawns:{}, moves:{}, winner:''};
  let pawns = data['state']['white_pawns'].concat(data['state']['black_pawns']);
  let moves = data.moves ? data.moves : [];

  pawns = make_id_keyed_object(pawns);
  for(let id in pawns){
    let pawn = pawns[id];
    let pawn_moves = moves.filter(move => move.pawn_id.toString() === id).map(move => move.id);
    let fieldKey = pawn.position.join(' ')
    let field = {"pawn":id, "fieldKey":fieldKey, "moves":pawn_moves}
    statePart.fields[fieldKey] = field;
  }
  moves = make_id_keyed_object(moves);

  statePart.moves = moves
  statePart.pawns = pawns

  return statePart;
}

function make_id_keyed_object(arr){
  let dono = {}
  for (let i=0; i<arr.length; i++){
    let id = arr[i].id
    dono[id] = arr[i]
    // delete dono[id].id
  }
  return dono;
}

export function stateFetchSuccess(data){
  return {
    type:constatns.STATE_FETCH_SUCCESS,
    fields: data.fields,
    pawns: data.pawns,
    moves: data.moves,
    winner: data.winner
  }
}

export function stateHasError(bool){
  return {
    type:constatns.STATE_HAS_ERROR,
    hasError:bool
  }
}

export function playerTurn(bool){
  return {
    type:constatns.PLAYER_TURN,
    playerTurn:bool
  }
}
