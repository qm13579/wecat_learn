// pages/list/list.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    newList:[],
    page:1,
    load:true,
    push:false
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function () {
    this.loadDate(this.data.page);
  },
  /**
   * 加载
   */
  loadDate:function(page){
    var _this = this;
    wx.request({
      url: 'http://127.0.0.1:8000/cms/',
      data: { page: page },
      success: function (res) {
        //判断是否为刷新，刷新则重置
        if(!_this.data.push){
          var data_list = _this.data.newList;
        }else{
          var data_list = [];
        }
        console.log(res.data);
        if (res.data==400){
          _this.setData({
            load:false
          })
        }else{
          for (var i = 0; i < res.data.length; i++) {
            res.data[i].fields.id = res.data[i].pk;
            res.data[i].fields.model = res.data[i].model;
            data_list.push(res.data[i].fields)
          };
        }
        _this.setData({
          newList: data_list,
          page :_this.data.page +1
        })
      }
    })
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    this.setData({
      push:true,
      page:1
    })
    console.log(this.data.push)
    this.loadDate(1);
    wx.stopPullDownRefresh();
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    if(this.data.load){
      console.log(this.data.load)
      console.log(this.data.page)
      console.log("上拉加载")
      this.loadDate(this.data.page);
      var num = this.data.page + 1;
      console.log(num)
    }else{
      console.log("已经加载完了")
    }
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})