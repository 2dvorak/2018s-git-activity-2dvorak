# Git Activity (Warm-up)

This is a repository created by Seung Yeop Lee (2dvorak) while
taking the course IS-521 2018 at KAIST.

## A simple program that randomly groupes class members

- `activity_warmup.py` takes in as input a CSV file and the number of maximum members in a group:

```
python activity_warmup.py [CSV FILE] [MAXIMUM MEMBERS IN A GROUP]
```

- Input CSV file contains two columns for (1) names, and (2) emails with no new line character in each field.

- Input number of maximum members in a group should be a integer greater than zero.

- Output will show a list of randomly grouped members:

```
$ python activity_warmup.py sample.csv 3
GROUP 1 : 'Dongman Lee' 'Brent Kang' 'Myungchul Kim'
GROUP 2 : 'Sang Kil Cha' 'Son, Sooel' 'Seungwon Shin'
GROUP 3 : 'Jooyoung Lee' 'Yongdae Kim' 'Kwangjo Kim
```

- Difference in number of group members not greater than 1 for fairness. For example:

```
$ python activity_warmup.py sample.csv 3
GROUP 1 : 'Myungchul Kim' 'Son, Sooel' 'Sang-Jin LEE'
GROUP 2 : 'Jooyoung Lee' 'Brent Kang' 'Sang Kil Cha'
GROUP 3 : 'Seungwon Shin' 'Yongdae Kim'
GROUP 4 : 'Kwangjo Kim' 'Dongman Lee'
```

### Prerequisite

- Python 2.7 (tested with Python 2.7.12 on Ubuntu 16.04 machine)
