import pandas as pd

class FlattenDict:
    def __init__(self):
        self.data_dic = {"id":[],"name":[], "address":[],
            "cuisines": [],"average_cost_for_two":[],
            "has_online_delivery":[], "locality": [],
            "city":[],"country_id":[], "zipcode":[],
            "aggregate_rating":[], "rating_text": [],
            "votes":[]
           }
    def get_data(self, data):
        """
        find out required data and return:
        """
        eval_data = eval(data)
        for i in eval_data:
            self.data_dic["id"].append(i["restaurant"]["id"])
            self.data_dic["name"].append(i["restaurant"]["name"])
            
            self.data_dic["cuisines"].append(i["restaurant"]["cuisines"])
            self.data_dic["average_cost_for_two"].append(i["restaurant"]["average_cost_for_two"])
            self.data_dic["has_online_delivery"].append(i["restaurant"]["has_online_delivery"])
            self.data_dic["aggregate_rating"].append(i["restaurant"]["user_rating"]["aggregate_rating"])
            self.data_dic["rating_text"].append(i["restaurant"]["user_rating"]["rating_text"])
            self.data_dic["votes"].append(i["restaurant"]["user_rating"]["votes"])
            ### location and address related data
            
            self.data_dic["address"].append(i["restaurant"]["location"]["address"])
            self.data_dic["locality"].append(i["restaurant"]["location"]["locality"])
            self.data_dic["city"].append(i["restaurant"]["location"]["city"])
            self.data_dic["country_id"].append(i["restaurant"]["location"]["country_id"])
            self.data_dic["zipcode"].append(i["restaurant"]["location"]["zipcode"])

    def convert_to_df(self):

        return pd.DataFrame(self.data_dic)
