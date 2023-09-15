{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8e98b065",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "da12a346",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv(\"Advertising.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "85867adf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>230.1</td>\n",
       "      <td>37.8</td>\n",
       "      <td>69.2</td>\n",
       "      <td>22.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>44.5</td>\n",
       "      <td>39.3</td>\n",
       "      <td>45.1</td>\n",
       "      <td>10.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>17.2</td>\n",
       "      <td>45.9</td>\n",
       "      <td>69.3</td>\n",
       "      <td>9.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>151.5</td>\n",
       "      <td>41.3</td>\n",
       "      <td>58.5</td>\n",
       "      <td>18.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>180.8</td>\n",
       "      <td>10.8</td>\n",
       "      <td>58.4</td>\n",
       "      <td>12.9</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0     TV  Radio  Newspaper  Sales\n",
       "0           1  230.1   37.8       69.2   22.1\n",
       "1           2   44.5   39.3       45.1   10.4\n",
       "2           3   17.2   45.9       69.3    9.3\n",
       "3           4  151.5   41.3       58.5   18.5\n",
       "4           5  180.8   10.8       58.4   12.9"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9975e365",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(\"Unnamed: 0\",axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b8bcd227",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>230.1</td>\n",
       "      <td>37.8</td>\n",
       "      <td>69.2</td>\n",
       "      <td>22.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>44.5</td>\n",
       "      <td>39.3</td>\n",
       "      <td>45.1</td>\n",
       "      <td>10.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>17.2</td>\n",
       "      <td>45.9</td>\n",
       "      <td>69.3</td>\n",
       "      <td>9.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>151.5</td>\n",
       "      <td>41.3</td>\n",
       "      <td>58.5</td>\n",
       "      <td>18.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>180.8</td>\n",
       "      <td>10.8</td>\n",
       "      <td>58.4</td>\n",
       "      <td>12.9</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      TV  Radio  Newspaper  Sales\n",
       "0  230.1   37.8       69.2   22.1\n",
       "1   44.5   39.3       45.1   10.4\n",
       "2   17.2   45.9       69.3    9.3\n",
       "3  151.5   41.3       58.5   18.5\n",
       "4  180.8   10.8       58.4   12.9"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d7f86882",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>200.000000</td>\n",
       "      <td>200.000000</td>\n",
       "      <td>200.000000</td>\n",
       "      <td>200.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>147.042500</td>\n",
       "      <td>23.264000</td>\n",
       "      <td>30.554000</td>\n",
       "      <td>14.022500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>85.854236</td>\n",
       "      <td>14.846809</td>\n",
       "      <td>21.778621</td>\n",
       "      <td>5.217457</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.700000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.300000</td>\n",
       "      <td>1.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>74.375000</td>\n",
       "      <td>9.975000</td>\n",
       "      <td>12.750000</td>\n",
       "      <td>10.375000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>149.750000</td>\n",
       "      <td>22.900000</td>\n",
       "      <td>25.750000</td>\n",
       "      <td>12.900000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>218.825000</td>\n",
       "      <td>36.525000</td>\n",
       "      <td>45.100000</td>\n",
       "      <td>17.400000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>296.400000</td>\n",
       "      <td>49.600000</td>\n",
       "      <td>114.000000</td>\n",
       "      <td>27.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               TV       Radio   Newspaper       Sales\n",
       "count  200.000000  200.000000  200.000000  200.000000\n",
       "mean   147.042500   23.264000   30.554000   14.022500\n",
       "std     85.854236   14.846809   21.778621    5.217457\n",
       "min      0.700000    0.000000    0.300000    1.600000\n",
       "25%     74.375000    9.975000   12.750000   10.375000\n",
       "50%    149.750000   22.900000   25.750000   12.900000\n",
       "75%    218.825000   36.525000   45.100000   17.400000\n",
       "max    296.400000   49.600000  114.000000   27.000000"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6e0a2035",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 200 entries, 0 to 199\n",
      "Data columns (total 4 columns):\n",
      " #   Column     Non-Null Count  Dtype  \n",
      "---  ------     --------------  -----  \n",
      " 0   TV         200 non-null    float64\n",
      " 1   Radio      200 non-null    float64\n",
      " 2   Newspaper  200 non-null    float64\n",
      " 3   Sales      200 non-null    float64\n",
      "dtypes: float64(4)\n",
      "memory usage: 6.4 KB\n"
     ]
    }
   ],
   "source": [
    "df.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5d9b046b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = sns.boxplot(df['TV'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "04686cde",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = sns.boxplot(df['Radio'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "87477fef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = sns.boxplot(df['Newspaper'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b435a539",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>67.8</td>\n",
       "      <td>36.6</td>\n",
       "      <td>114.0</td>\n",
       "      <td>12.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101</th>\n",
       "      <td>296.4</td>\n",
       "      <td>36.3</td>\n",
       "      <td>100.9</td>\n",
       "      <td>23.8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        TV  Radio  Newspaper  Sales\n",
       "16    67.8   36.6      114.0   12.5\n",
       "101  296.4   36.3      100.9   23.8"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df[\"Newspaper\"]>=100]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c814e57d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(index=[16,101],axis=0,inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "681d47a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>230.1</td>\n",
       "      <td>37.8</td>\n",
       "      <td>69.2</td>\n",
       "      <td>22.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>44.5</td>\n",
       "      <td>39.3</td>\n",
       "      <td>45.1</td>\n",
       "      <td>10.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>17.2</td>\n",
       "      <td>45.9</td>\n",
       "      <td>69.3</td>\n",
       "      <td>9.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>151.5</td>\n",
       "      <td>41.3</td>\n",
       "      <td>58.5</td>\n",
       "      <td>18.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>180.8</td>\n",
       "      <td>10.8</td>\n",
       "      <td>58.4</td>\n",
       "      <td>12.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>8.7</td>\n",
       "      <td>48.9</td>\n",
       "      <td>75.0</td>\n",
       "      <td>7.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>57.5</td>\n",
       "      <td>32.8</td>\n",
       "      <td>23.5</td>\n",
       "      <td>11.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>120.2</td>\n",
       "      <td>19.6</td>\n",
       "      <td>11.6</td>\n",
       "      <td>13.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>8.6</td>\n",
       "      <td>2.1</td>\n",
       "      <td>1.0</td>\n",
       "      <td>4.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>199.8</td>\n",
       "      <td>2.6</td>\n",
       "      <td>21.2</td>\n",
       "      <td>10.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>66.1</td>\n",
       "      <td>5.8</td>\n",
       "      <td>24.2</td>\n",
       "      <td>8.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>214.7</td>\n",
       "      <td>24.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>17.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>23.8</td>\n",
       "      <td>35.1</td>\n",
       "      <td>65.9</td>\n",
       "      <td>9.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>97.5</td>\n",
       "      <td>7.6</td>\n",
       "      <td>7.2</td>\n",
       "      <td>9.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>204.1</td>\n",
       "      <td>32.9</td>\n",
       "      <td>46.0</td>\n",
       "      <td>19.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>195.4</td>\n",
       "      <td>47.7</td>\n",
       "      <td>52.9</td>\n",
       "      <td>22.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>281.4</td>\n",
       "      <td>39.6</td>\n",
       "      <td>55.8</td>\n",
       "      <td>24.4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       TV  Radio  Newspaper  Sales\n",
       "0   230.1   37.8       69.2   22.1\n",
       "1    44.5   39.3       45.1   10.4\n",
       "2    17.2   45.9       69.3    9.3\n",
       "3   151.5   41.3       58.5   18.5\n",
       "4   180.8   10.8       58.4   12.9\n",
       "5     8.7   48.9       75.0    7.2\n",
       "6    57.5   32.8       23.5   11.8\n",
       "7   120.2   19.6       11.6   13.2\n",
       "8     8.6    2.1        1.0    4.8\n",
       "9   199.8    2.6       21.2   10.6\n",
       "10   66.1    5.8       24.2    8.6\n",
       "11  214.7   24.0        4.0   17.4\n",
       "12   23.8   35.1       65.9    9.2\n",
       "13   97.5    7.6        7.2    9.7\n",
       "14  204.1   32.9       46.0   19.0\n",
       "15  195.4   47.7       52.9   22.4\n",
       "17  281.4   39.6       55.8   24.4"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[0:17][:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "acf92018",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=df.reset_index()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ae30fd92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>230.1</td>\n",
       "      <td>37.8</td>\n",
       "      <td>69.2</td>\n",
       "      <td>22.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>44.5</td>\n",
       "      <td>39.3</td>\n",
       "      <td>45.1</td>\n",
       "      <td>10.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>17.2</td>\n",
       "      <td>45.9</td>\n",
       "      <td>69.3</td>\n",
       "      <td>9.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>151.5</td>\n",
       "      <td>41.3</td>\n",
       "      <td>58.5</td>\n",
       "      <td>18.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>180.8</td>\n",
       "      <td>10.8</td>\n",
       "      <td>58.4</td>\n",
       "      <td>12.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>5</td>\n",
       "      <td>8.7</td>\n",
       "      <td>48.9</td>\n",
       "      <td>75.0</td>\n",
       "      <td>7.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>6</td>\n",
       "      <td>57.5</td>\n",
       "      <td>32.8</td>\n",
       "      <td>23.5</td>\n",
       "      <td>11.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>7</td>\n",
       "      <td>120.2</td>\n",
       "      <td>19.6</td>\n",
       "      <td>11.6</td>\n",
       "      <td>13.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>8</td>\n",
       "      <td>8.6</td>\n",
       "      <td>2.1</td>\n",
       "      <td>1.0</td>\n",
       "      <td>4.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>9</td>\n",
       "      <td>199.8</td>\n",
       "      <td>2.6</td>\n",
       "      <td>21.2</td>\n",
       "      <td>10.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>10</td>\n",
       "      <td>66.1</td>\n",
       "      <td>5.8</td>\n",
       "      <td>24.2</td>\n",
       "      <td>8.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>11</td>\n",
       "      <td>214.7</td>\n",
       "      <td>24.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>17.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>12</td>\n",
       "      <td>23.8</td>\n",
       "      <td>35.1</td>\n",
       "      <td>65.9</td>\n",
       "      <td>9.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>13</td>\n",
       "      <td>97.5</td>\n",
       "      <td>7.6</td>\n",
       "      <td>7.2</td>\n",
       "      <td>9.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>14</td>\n",
       "      <td>204.1</td>\n",
       "      <td>32.9</td>\n",
       "      <td>46.0</td>\n",
       "      <td>19.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>15</td>\n",
       "      <td>195.4</td>\n",
       "      <td>47.7</td>\n",
       "      <td>52.9</td>\n",
       "      <td>22.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>17</td>\n",
       "      <td>281.4</td>\n",
       "      <td>39.6</td>\n",
       "      <td>55.8</td>\n",
       "      <td>24.4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    index     TV  Radio  Newspaper  Sales\n",
       "0       0  230.1   37.8       69.2   22.1\n",
       "1       1   44.5   39.3       45.1   10.4\n",
       "2       2   17.2   45.9       69.3    9.3\n",
       "3       3  151.5   41.3       58.5   18.5\n",
       "4       4  180.8   10.8       58.4   12.9\n",
       "5       5    8.7   48.9       75.0    7.2\n",
       "6       6   57.5   32.8       23.5   11.8\n",
       "7       7  120.2   19.6       11.6   13.2\n",
       "8       8    8.6    2.1        1.0    4.8\n",
       "9       9  199.8    2.6       21.2   10.6\n",
       "10     10   66.1    5.8       24.2    8.6\n",
       "11     11  214.7   24.0        4.0   17.4\n",
       "12     12   23.8   35.1       65.9    9.2\n",
       "13     13   97.5    7.6        7.2    9.7\n",
       "14     14  204.1   32.9       46.0   19.0\n",
       "15     15  195.4   47.7       52.9   22.4\n",
       "16     17  281.4   39.6       55.8   24.4"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[0:17][:]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "c11131c4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax=sns.boxplot(df[\"Newspaper\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f0022d40",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "index        0\n",
       "TV           0\n",
       "Radio        0\n",
       "Newspaper    0\n",
       "Sales        0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "e990f98f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>230.1</td>\n",
       "      <td>37.8</td>\n",
       "      <td>69.2</td>\n",
       "      <td>22.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>44.5</td>\n",
       "      <td>39.3</td>\n",
       "      <td>45.1</td>\n",
       "      <td>10.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>17.2</td>\n",
       "      <td>45.9</td>\n",
       "      <td>69.3</td>\n",
       "      <td>9.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>151.5</td>\n",
       "      <td>41.3</td>\n",
       "      <td>58.5</td>\n",
       "      <td>18.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>180.8</td>\n",
       "      <td>10.8</td>\n",
       "      <td>58.4</td>\n",
       "      <td>12.9</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index     TV  Radio  Newspaper  Sales\n",
       "0      0  230.1   37.8       69.2   22.1\n",
       "1      1   44.5   39.3       45.1   10.4\n",
       "2      2   17.2   45.9       69.3    9.3\n",
       "3      3  151.5   41.3       58.5   18.5\n",
       "4      4  180.8   10.8       58.4   12.9"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "46838d2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(\"index\",axis=1,inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "b719c98e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>230.1</td>\n",
       "      <td>37.8</td>\n",
       "      <td>69.2</td>\n",
       "      <td>22.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>44.5</td>\n",
       "      <td>39.3</td>\n",
       "      <td>45.1</td>\n",
       "      <td>10.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>17.2</td>\n",
       "      <td>45.9</td>\n",
       "      <td>69.3</td>\n",
       "      <td>9.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>151.5</td>\n",
       "      <td>41.3</td>\n",
       "      <td>58.5</td>\n",
       "      <td>18.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>180.8</td>\n",
       "      <td>10.8</td>\n",
       "      <td>58.4</td>\n",
       "      <td>12.9</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      TV  Radio  Newspaper  Sales\n",
       "0  230.1   37.8       69.2   22.1\n",
       "1   44.5   39.3       45.1   10.4\n",
       "2   17.2   45.9       69.3    9.3\n",
       "3  151.5   41.3       58.5   18.5\n",
       "4  180.8   10.8       58.4   12.9"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "f728948e",
   "metadata": {},
   "outputs": [],
   "source": [
    "y=df[\"Sales\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "af80d980",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=df.drop(\"Sales\",axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "19fd5356",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>230.1</td>\n",
       "      <td>37.8</td>\n",
       "      <td>69.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>44.5</td>\n",
       "      <td>39.3</td>\n",
       "      <td>45.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>17.2</td>\n",
       "      <td>45.9</td>\n",
       "      <td>69.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>151.5</td>\n",
       "      <td>41.3</td>\n",
       "      <td>58.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>180.8</td>\n",
       "      <td>10.8</td>\n",
       "      <td>58.4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      TV  Radio  Newspaper\n",
       "0  230.1   37.8       69.2\n",
       "1   44.5   39.3       45.1\n",
       "2   17.2   45.9       69.3\n",
       "3  151.5   41.3       58.5\n",
       "4  180.8   10.8       58.4"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "7bb1df25",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    22.1\n",
       "1    10.4\n",
       "2     9.3\n",
       "3    18.5\n",
       "4    12.9\n",
       "Name: Sales, dtype: float64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "99d2ecf1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "a3a9ebaf",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=43)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "1a242a00",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((132, 3), (66, 3), (132,), (66,))"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train.shape,x_test.shape,y_train.shape,y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "56bbaa48",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "17ab7611",
   "metadata": {},
   "outputs": [],
   "source": [
    "ss=StandardScaler()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "f373f4be",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train=ss.fit_transform(x_train)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "a039e122",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_test=ss.transform(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "1eac0b52",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.tree import DecisionTreeRegressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "4bb4be6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "dt=DecisionTreeRegressor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "5ac9b6bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "model=dt.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "eee291a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_predicted=dt.predict(x_test)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "d3fdb5b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import r2_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "6d557b8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "score=r2_score(y_test,y_predicted)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "8ff9f7c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9338766309109264"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38313acd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
