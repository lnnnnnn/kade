        if("undefined"!=e.info&&"w is not number"==e.info)return console.log("w is not number"),c.a.error("w 非数值类型！"),void r.setState({tripleSchemaSelectModalVisible:!1,selectedTripleSchema:null,selectedTripleSchema2:null,tripleSchemas:[]});

        var n=e.triple;r.setState({tripleSchemaSelectModalVisible:!1,selectedTripleSchema:null,selectedTripleSchema2:null,tripleSchemas:[]});var o=r.tripleToRelationship(n);r.afterTripleSchemaSelectionCallback(null,{relationships:[o]}),r.afterTripleSchemaSelectionCallback=null,r.subject=null,r.object=null,setTimeout(function(){i.setState({triples:f()(t).concat([n])})},100)}}).catch(function(e){console.error(e.message)})},r.onTripleSchemaChange=function(e){r.setState({selectedTripleSchema:e.target.value})},r.onTripleSchemaChange2=function(e){r.setState({selectedTripleSchema2:e.target.value})},r.onNodeClose=function(e){setTimeout(function(){var t=r.state,n=t.triples,o=t.entities,i=o.filter(function(t){return t._id!==e.id}),a=n.filter(function(t){return t.s!==e.id&&t.o!==e.id});r.setState({entities:i,triples:a})},100)},r.entityToNode=function(e){return{id:e._id,labels:[e._schema.name],properties:a()({},e._schema.properties[0].name,e[e._schema.properties[0].name])}},r.tripleToRelationship=function(e){return{id:e._id,startNodeId:e.s,endNodeId:e.o,type:e.p,properties:{}}},n))}return M()(t,[{key:"render",value:function(){var e=this,t=this.state,n=t.entities,i=t.triples,a=t.tripleSchemaSelectModalVisible,c=(t.selectedTripleSchema,t.selectedTripleSchema2,t.tripleSchemas,[]),s=[];n&&n.length>0&&(c=n.map(function(t){return e.entityToNode(t)})),i&&i.length>0&&(s=i.map(function(t){return e.tripleToRelationship(t)}));return D.a.createElement("div",{style:{position:"relative",height:"100%"}},D.a.createElement(r.a,{title:"\u8f93\u5165\u5173\u7cfb",visible:a,onOk:this.selectTripleSchema.bind(this),onCancel:function(){return e.setState({tripleSchemaSelectModalVisible:!1})},okText:"\u786e\u8ba4",cancelText:"\u53d6\u6d88"},D.a.createElement(o.a,{placeholder:"\u8f93\u5165\u7c7b\u578b(tp)",value:this.state.selectedTripleSchema,onChange:this.onTripleSchemaChange.bind(this),onPressEnter:this.selectTripleSchema.bind(this),style:{marginBottom:"20px"}}),D.a.createElement(o.a,{placeholder:"\u8f93\u5165\u6743\u91cd(w)",value:this.state.selectedTripleSchema2,onChange:this.onTripleSchemaChange2.bind(this),onPressEnter:this.selectTripleSchema.bind(this)})),D.a.createElement(S.a,{theme:T.a},D.a.createElement(k.a,{editable:!0,maxNeighbours:100,initialNodeDisplay:300,updateStyle:function(){},getNeighbours:this.getNeighbours.bind(this),nodes:c,relationships:s,fullscreen:!1,frameHeight:50,assignVisElement:function(t,n){e.visElement={svgElement:t,graphElement:n,type:"graph"}},getAutoCompleteCallback:function(t){e.autoCompleteCallback=t},setGraph:this.setGraph.bind(this),onSearchEntity:this.onSearchEntity.bind(this),onNewEntity:this.onNewEntity.bind(this),onEditEntity:this.onEditEntity.bind(this),onNodeClose:this.onNodeClose.bind(this),onAddRelationship:this.onAddRelationship.bind(this),onItemRemove:this.onItemRemove.bind(this),entities:n})))}}]),g()(t,e),t}(z.PureComponent))},"zo/l":function(e,t,n){var r=n("oeih"),o=Math.max,i=Math.min;e.exports=function(e,t){return e=r(e),e<0?o(e+t,0):i(e,t)}},zovc:function(e,t,n){"use strict";function r(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function o(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function i(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}var a=n("BYKG"),c=a.Record,s={anchorKey:"",anchorOffset:0,focusKey:"",focusOffset:0,isBackward:!1,hasFocus:!1},l=c(s),u=function(e){function t(){return r(this,t),o(this,e.apply(this,arguments))}return i(t,e),t.prototype.serialize=function(){return"Anchor: "+this.getAnchorKey()+":"+this.getAnchorOffset()+", Focus: "+this.getFocusKey()+":"+this.getFocusOffset()+", Is Backward: "+String(this.getIsBackward())+", Has Focus: "+String(this.getHasFocus())},t.prototype.getAnchorKey=function(){return this.get("anchorKey")},t.prototype.getAnchorOffset=function(){return this.get("anchorOffset")},t.prototype.getFocusKey=function(){return this.get("focusKey")},t.prototype.getFocusOffset=function(){return this.get("focusOffset")},t.prototype.getIsBackward=function(){return this.get("isBackward")},t.prototype.getHasFocus=function(){return this.get("hasFocus")},t.prototype.hasEdgeWithin=function(e,t,n){var r=this.getAnchorKey(),o=this.getFocusKey();if(r===o&&r===e){var i=this.getStartOffset();return t<=this.getEndOffset()&&i<=n}if(e!==r&&e!==o)return!1;var a=e===r?this.getAnchorOffset():this.getFocusOffset();return t<=a&&n>=a},t.prototype.isCollapsed=function(){return this.getAnchorKey()===this.getFocusKey()&&this.getAnchorOffset()===this.getFocusOffset()},t.prototype.getStartKey=function(){return this.getIsBackward()?this.getFocusKey():this.getAnchorKey()},t.prototype.getStartOffset=function(){return this.getIsBackward()?this.getFocusOffset():this.getAnchorOffset()},t.prototype.getEndKey=function(){return this.getIsBackward()?this.getAnchorKey():this.getFocusKey()},t.prototype.getEndOffset=function(){return this.getIsBackward()?this.getAnchorOffset():this.getFocusOffset()},t.createEmpty=function(e){return new t({anchorKey:e,anchorOffset:0,focusKey:e,focusOffset:0,isBackward:!1,hasFocus:!1})},t}(l);e.exports=u},zpVT:function(e,t,n){function r(e,t){var n=this.__data__;if(n instanceof o){var r=n.__data__;if(!i||r.length<c-1)return r.push([e,t]),this.size=++n.size,this;n=this.__data__=new a(r)}return n.set(e,t),this.size=n.size,this}var o=n("duB3"),i=n("POb3"),a=n("YeCl"),c=200;e.exports=r},"zq/X":function(e,t,n){var r=n("UKM+");e.exports=function(e,t){if(!r(e)||e._t!==t)throw TypeError("Incompatible receiver, "+t+" required!");return e}},zwGx:function(e,t,n){"use strict";function r(e){return"string"==typeof e}function o(e,t){if(null!=e){var n=t?" ":"";return"string"!=typeof e&&"number"!=typeof e&&r(e.type)&&E(e.props.children)?g.cloneElement(e,{},e.props.children.split("").join(n)):"string"==typeof e?(E(e)&&(e=e.split("").join(n)),g.createElement("span",null,e)):e}}var i=n("Dd8w"),a=n.n(i),c=n("bOdI"),s=n.n(c),l=n("Zrlr"),u=n.n(l),f=n("wxAW"),p=n.n(f),d=n("zwoO"),h=n.n(d),v=n("Pf15"),m=n.n(v),g=n("GiK3"),y=n("KSGD"),M=n("HW6M"),b=n.n(M),w=n("J7eb"),C=n("FC3+"),x=this&&this.__rest||function(e,t){var n={};for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&t.indexOf(r)<0&&(n[r]=e[r]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols)for(var o=0,r=Object.getOwnPropertySymbols(e);o<r.length;o++)t.indexOf(r[o])<0&&(n[r[o]]=e[r[o]]);return n},N=/^[\u4e00-\u9fa5]{2}$/,E=N.test.bind(N),O=function(e){function t(e){u()(this,t);var n=h()(this,(t.__proto__||Object.getPrototypeOf(t)).call(this,e));return n.saveButtonRef=function(e){n.buttonNode=e},n.handleClick=function(e){var t=n.state.loading,r=n.props.onClick;t||r&&r(e)},n.state={loading:e.loading,hasTwoCNChar:!1},n}return m()(t,e),p()(t,[{key:"componentDidMount",value:function(){this.fixTwoCNChar()}},{key:"componentWillReceiveProps",value:function(e){var t=this,n=this.props.loading,r=e.loading;n&&clearTimeout(this.delayTimeout),"boolean"!=typeof r&&r&&r.delay?this.delayTimeout=window.setTimeout(function(){return t.setState({loading:r})},r.delay):this.setState({loading:r})}},{key:"componentDidUpdate",value:function(){this.fixTwoCNChar()}},{key:"componentWillUnmount",value:function(){this.delayTimeout&&clearTimeout(this.delayTimeout)}},{key:"fixTwoCNChar",value:function(){if(this.buttonNode){var e=this.buttonNode.textContent||this.buttonNode.innerText;this.isNeedInserted()&&E(e)?this.state.hasTwoCNChar||this.setState({hasTwoCNChar:!0}):this.state.hasTwoCNChar&&this.setState({hasTwoCNChar:!1})}}},{key:"isNeedInserted",value:function(){var e=this.props,t=e.icon,n=e.children;return 1===g.Children.count(n)&&!t}},{key:"render",value:function(){var e,t=this,n=this.props,r=n.type,i=n.shape,c=n.size,l=n.className,u=n.children,f=n.icon,p=n.prefixCls,d=n.ghost,h=(n.loading,n.block),v=x(n,["type","shape","size","className","children","icon","prefixCls","ghost","loading","block"]),m=this.state,y=m.loading,M=m.hasTwoCNChar,N="";switch(c){case"large":N="lg";break;case"small":N="sm"}var E=new Date,O=11===E.getMonth()&&25===E.getDate(),z=b()(p,l,(e={},s()(e,p+"-"+r,r),s()(e,p+"-"+i,i),s()(e,p+"-"+N,N),s()(e,p+"-icon-only",!u&&f),s()(e,p+"-loading",y),s()(e,p+"-background-ghost",d),s()(e,p+"-two-chinese-chars",M),s()(e,p+"-block",h),s()(e,"christmas",O),e)),D=y?"loading":f,S=D?g.createElement(C.a,{type:D}):null,k=u||0===u?g.Children.map(u,function(e){return o(e,t.isNeedInserted())}):null,T=O?"Ho Ho Ho!":v.title;if("href"in v)return g.createElement("a",a()({},v,{className:z,onClick:this.handleClick,title:T,ref:this.saveButtonRef}),S,k);var I=v.htmlType,A=x(v,["htmlType"]);return g.createElement(w.a,null,g.createElement("button",a()({},A,{type:I||"button",className:z,onClick:this.handleClick,title:T,ref:this.saveButtonRef}),S,k))}}]),t}(g.Component),z=O;O.__ANT_BUTTON=!0,O.defaultProps={prefixCls:"ant-btn",loading:!1,ghost:!1,block:!1},O.propTypes={type:y.string,shape:y.oneOf(["circle","circle-outline"]),size:y.oneOf(["large","default","small"]),htmlType:y.oneOf(["submit","button","reset"]),onClick:y.func,loading:y.oneOfType([y.bool,y.object]),className:y.string,icon:y.string,block:y.bool};var D=this&&this.__rest||function(e,t){var n={};for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&t.indexOf(r)<0&&(n[r]=e[r]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols)for(var o=0,r=Object.getOwnPropertySymbols(e);o<r.length;o++)t.indexOf(r[o])<0&&(n[r[o]]=e[r[o]]);return n},S=function(e){var t=e.prefixCls,n=void 0===t?"ant-btn-group":t,r=e.size,o=e.className,i=D(e,["prefixCls","size","className"]),c="";switch(r){case"large":c="lg";break;case"small":c="sm"}var l=b()(n,s()({},n+"-"+c,c),o);return g.createElement("div",a()({},i,{className:l}))},k=S;z.Group=k;t.a=z},zwoO:function(e,t,n){"use strict";t.__esModule=!0;var r=n("pFYg"),o=function(e){return e&&e.__esModule?e:{default:e}}(r);t.default=function(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!==(void 0===t?"undefined":(0,o.default)(t))&&"function"!=typeof t?e:t}}});