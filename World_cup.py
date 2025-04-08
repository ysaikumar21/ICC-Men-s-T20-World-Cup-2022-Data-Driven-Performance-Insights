'''this we are develop the program for ICC Men's T20 World Cup 2022 Analysis using python programming'''
import numpy as np
import pandas as pd
import sys
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

class ICC_MEN_WORLD_CUP:
    def __init__(self,world_cup):
        try:
            pio.templates.default ='plotly_white'
            self.world_cup=world_cup
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f"Error from Line {err_line.tblineno} -> type {error_type.__name__} -> Error msg -> {error_msg}")
    def Each_team_wins(self):
        try:
            Figure=px.bar(self.world_cup,
            x=self.world_cup['winner'],
            title="Number of Maches Win By Teams in T20 World Cup 2022"
            )
            Figure.show()
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f"Error from Line {err_line.tblineno} -> type {error_type.__name__} -> Error msg -> {error_msg}")

    def Batting_fir_sec_win(self):
        try:
            won_by = self.world_cup["won by"].value_counts()
            label = won_by.index
            counts = won_by.values
            colors = ['gold','lightgreen']
            fig = go.Figure(data=[go.Pie(labels=label, values=counts, hoverinfo='label+percent')])
            fig.update_layout(title_text='Number of Matches Won By Runs Or Wickets')
            fig.show()
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f"Error from Line {err_line.tblineno} -> type {error_type.__name__} -> Error msg -> {error_msg}")   

    def toss_win_bat_bow(self):
        try:
            toss=self.world_cup["toss decision"].value_counts()
            label=toss.index
            counts=toss.values
            colors=['skyblue','yellow']
            fig = go.Figure(data=[go.Pie(labels=label, values=counts, hoverinfo='label+percent')])
            fig.update_layout(title_text='Toss Decisions in t20 Worlds Cup 2022')
            fig.show()
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f"Error from Line {err_line.tblineno} -> type {error_type.__name__} -> Error msg -> {error_msg}")
    def Top_scorers(self):
        try:
            fig=px.bar(self.world_cup,
            x=self.world_cup["top scorer"],
            y=self.world_cup["highest score"],
            color=self.world_cup["highest score"],
            title="Top Scorers in T20 World Cup 2022")
            fig.show()
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f"Error from Line {err_line.tblineno} -> type {error_type.__name__} -> Error msg -> {error_msg}")

    def Player_of_match_awards(self):
        try:
            fig=px.bar(self.world_cup,
            x=self.world_cup["player of the match"],
            title="Player Of The Match Awards In T20 World Cup 2022")
            fig.show()
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f"Error from Line {err_line.tblineno} -> type {error_type.__name__} -> Error msg -> {error_msg}")
    def Best_bowlers(self):
        try:
            fig=px.bar(self.world_cup,
            x=self.world_cup["best bowler"],
            title="Best Bowlers in The T20 World Cup 2022")
            fig.show()
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f"Error from Line {err_line.tblineno} -> type {error_type.__name__} -> Error msg -> {error_msg}")
    def Best_Stadium_Batting(self):
        try:
            fig=go.Figure()
            fig.add_trace(go.Bar(
                x=self.world_cup["venue"],
                y=self.world_cup["first innings score"],
                name="First Innings Runs",
                marker_color='blue'
            ))
            fig.add_trace(go.Bar(
                x=self.world_cup["venue"],
                y=self.world_cup["second innings score"],
                name="Second Innings Runs",
                marker_color='red'
            ))
            fig.update_layout(barmode='group',
            xaxis_tickangle=-45,
            title="Best Stadiums For First Batting or Chase")
            fig.show()
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f"Error from Line {err_line.tblineno} -> type {error_type.__name__} -> Error msg -> {error_msg}")

    def Best_Stadium_Bowling(self):
        try:
            fig=go.Figure()
            fig.add_trace(go.Bar(
                x=self.world_cup["venue"],
                y=self.world_cup["first innings wickets"],
                name="First Innings Wickets",
                marker_color='blue'
            ))
            fig.add_trace(go.Bar(
                x=self.world_cup["venue"],
                y=self.world_cup["second innings wickets"],
                name="Second Innings Wickets",
                marker_color="red"
            ))
            fig.update_layout(barmode="group",
            xaxis_tickangle=-50,
            title="Best Stadium For Bowling First Or Defend")
            fig.show()
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f"Error from Line {err_line.tblineno} -> type {error_type.__name__} -> Error msg -> {error_msg}")

if __name__=='__main__':
    try:
        object=ICC_MEN_WORLD_CUP(world_cup=pd.read_csv("C:\\Users\\Saiku\\Downloads\\ICC Men’s T20 World Cup 2022 Analysis\\t20-world-cup-22.csv"))
        object.Each_team_wins()
        object.Batting_fir_sec_win()
        object.toss_win_bat_bow()
        object.Top_scorers()
        object.Player_of_match_awards()
        object.Best_bowlers()
        object.Best_Stadium_Batting()
        object.Best_Stadium_Bowling()
    except Exception as e:
        error_type, error_msg, err_line = sys.exc_info()
        print(f"Error from Line {err_line.tblineno} -> type {error_type.__name__} -> Error msg -> {error_msg}")
