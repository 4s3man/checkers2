/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./pages/choose_game/index.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./node_modules/reset-css/reset.css":
/*!******************************************!*\
  !*** ./node_modules/reset-css/reset.css ***!
  \******************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("// extracted by mini-css-extract-plugin//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9ub2RlX21vZHVsZXMvcmVzZXQtY3NzL3Jlc2V0LmNzcy5qcyIsInNvdXJjZXMiOlsid2VicGFjazovLy8uL25vZGVfbW9kdWxlcy9yZXNldC1jc3MvcmVzZXQuY3NzP2VkNWUiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gZXh0cmFjdGVkIGJ5IG1pbmktY3NzLWV4dHJhY3QtcGx1Z2luIl0sIm1hcHBpbmdzIjoiQUFBQSIsInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./node_modules/reset-css/reset.css\n");

/***/ }),

/***/ "./pages/choose_game/bundle_styles.js":
/*!********************************************!*\
  !*** ./pages/choose_game/bundle_styles.js ***!
  \********************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
eval("\n\n__webpack_require__(/*! reset-css */ \"./node_modules/reset-css/reset.css\");\n\n__webpack_require__(/*! ../shared_css/base.css */ \"./pages/shared_css/base.css\");\n\n__webpack_require__(/*! ./css/positioning.css */ \"./pages/choose_game/css/positioning.css\");//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9wYWdlcy9jaG9vc2VfZ2FtZS9idW5kbGVfc3R5bGVzLmpzLmpzIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vL3BhZ2VzL2Nob29zZV9nYW1lL2J1bmRsZV9zdHlsZXMuanM/NzM4NSJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgXCJyZXNldC1jc3NcIlxuaW1wb3J0IFwiLi4vc2hhcmVkX2Nzcy9iYXNlLmNzc1wiXG5pbXBvcnQgXCIuL2Nzcy9wb3NpdGlvbmluZy5jc3NcIlxuIl0sIm1hcHBpbmdzIjoiOztBQUFBO0FBQ0E7QUFBQTtBQUNBO0FBQUEiLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./pages/choose_game/bundle_styles.js\n");

/***/ }),

/***/ "./pages/choose_game/css/positioning.css":
/*!***********************************************!*\
  !*** ./pages/choose_game/css/positioning.css ***!
  \***********************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("// extracted by mini-css-extract-plugin//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9wYWdlcy9jaG9vc2VfZ2FtZS9jc3MvcG9zaXRpb25pbmcuY3NzLmpzIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vLy4vcGFnZXMvY2hvb3NlX2dhbWUvY3NzL3Bvc2l0aW9uaW5nLmNzcz82NTA5Il0sInNvdXJjZXNDb250ZW50IjpbIi8vIGV4dHJhY3RlZCBieSBtaW5pLWNzcy1leHRyYWN0LXBsdWdpbiJdLCJtYXBwaW5ncyI6IkFBQUEiLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./pages/choose_game/css/positioning.css\n");

/***/ }),

/***/ "./pages/choose_game/index.js":
/*!************************************!*\
  !*** ./pages/choose_game/index.js ***!
  \************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
eval("\n\n__webpack_require__(/*! ./bundle_styles.js */ \"./pages/choose_game/bundle_styles.js\");\n\nvar socket = io.connect('http://' + document.domain + ':' + location.port); //io attached in script above in layout.html\n\n\nsocket.on('connect', function () {\n    console.log('Websocket connected!');\n    socket.emit('create', {});\n});//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9wYWdlcy9jaG9vc2VfZ2FtZS9pbmRleC5qcy5qcyIsInNvdXJjZXMiOlsid2VicGFjazovLy9wYWdlcy9jaG9vc2VfZ2FtZS9pbmRleC5qcz8zNDA5Il0sInNvdXJjZXNDb250ZW50IjpbIi8vaW8gYXR0YWNoZWQgaW4gc2NyaXB0IGFib3ZlIGluIGxheW91dC5odG1sXG5pbXBvcnQgXCIuL2J1bmRsZV9zdHlsZXMuanNcIlxuXG52YXIgc29ja2V0ID0gaW8uY29ubmVjdCgnaHR0cDovLycgKyBkb2N1bWVudC5kb21haW4gKyAnOicgKyBsb2NhdGlvbi5wb3J0KTtcblxuc29ja2V0Lm9uKCdjb25uZWN0JywgZnVuY3Rpb24oKSB7XG4gICAgY29uc29sZS5sb2coJ1dlYnNvY2tldCBjb25uZWN0ZWQhJyk7XG4gICAgc29ja2V0LmVtaXQoJ2NyZWF0ZScsIHt9KVxufSk7XG4iXSwibWFwcGluZ3MiOiI7O0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUFBO0FBQ0E7QUFDQTtBQUNBIiwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./pages/choose_game/index.js\n");

/***/ }),

/***/ "./pages/shared_css/base.css":
/*!***********************************!*\
  !*** ./pages/shared_css/base.css ***!
  \***********************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("// extracted by mini-css-extract-plugin//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9wYWdlcy9zaGFyZWRfY3NzL2Jhc2UuY3NzLmpzIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vLy4vcGFnZXMvc2hhcmVkX2Nzcy9iYXNlLmNzcz8zNzg5Il0sInNvdXJjZXNDb250ZW50IjpbIi8vIGV4dHJhY3RlZCBieSBtaW5pLWNzcy1leHRyYWN0LXBsdWdpbiJdLCJtYXBwaW5ncyI6IkFBQUEiLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./pages/shared_css/base.css\n");

/***/ })

/******/ });