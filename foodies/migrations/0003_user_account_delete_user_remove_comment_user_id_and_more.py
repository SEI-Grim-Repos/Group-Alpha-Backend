# Generated by Django 4.1.7 on 2023-02-16 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foodies', '0002_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('AFGHANISTAN', 'AF'), ('ALBANIA', 'AL'), ('ALGERIA', 'DZ'), ('AMERICAN SAMOA', 'AS'), ('ANDORRA', 'AD'), ('ANGOLA', 'AO'), ('ANGUILLA', 'AI'), ('ANTARCTICA', 'AQ'), ('ANTIGUA AND BARBUDA', 'AG'), ('ARGENTINA', 'AR'), ('ARMENIA', 'AM'), ('ARUBA', 'AW'), ('AUSTRALIA', 'AU'), ('AUSTRIA', 'AT'), ('AZERBAIJAN', 'AZ'), ('BAHAMAS', 'BS'), ('BAHRAIN', 'BH'), ('BANGLADESH', 'BD'), ('BARBADOS', 'BB'), ('BELARUS', 'BY'), ('BELGIUM', 'BE'), ('BELIZE', 'BZ'), ('BENIN', 'BJ'), ('BERMUDA', 'BM'), ('BHUTAN', 'BT'), ('BOLIVIA', 'BO'), ('BOSNIA AND HERZEGOVINA', 'BA'), ('BOTSWANA', 'BW'), ('BOUVET ISLAND', 'BV'), ('BRAZIL', 'BR'), ('BRITISH INDIAN OCEAN TERRITORY', 'IO'), ('BRUNEI DARUSSALAM', 'BN'), ('BULGARIA', 'BG'), ('BURKINA FASO', 'BF'), ('BURUNDI', 'BI'), ('CAMBODIA', 'KH'), ('CAMEROON', 'CM'), ('CANADA', 'CA'), ('CAPE VERDE', 'CV'), ('CAYMAN ISLANDS', 'KY'), ('CENTRAL AFRICAN REPUBLIC', 'CF'), ('CHAD', 'TD'), ('CHILE', 'CL'), ('CHINA', 'CN'), ('CHRISTMAS ISLAND', 'CX'), ('COCOS ISLANDS', 'CC'), ('COLOMBIA', 'CO'), ('COMOROS', 'KM'), ('CONGO', 'CG'), ('CONGO, THE DEMOCRATIC REPUBLIC OF', 'CD'), ('COOK ISLANDS', 'CK'), ('COSTA RICA', 'CR'), ("CÃ”TE D'IVOIRE", 'CI'), ('CROATIA', 'HR'), ('CUBA', 'CU'), ('CYPRUS', 'CY'), ('CZECH REPUBLIC', 'CZ'), ('DENMARK', 'DK'), ('DJIBOUTI', 'DJ'), ('DOMINICA', 'DM'), ('DOMINICAN REPUBLIC', 'DO'), ('ECUADOR', 'EC'), ('EGYPT', 'EG'), ('EL SALVADOR', 'SV'), ('EQUATORIAL GUINEA', 'GQ'), ('ERITREA', 'ER'), ('ESTONIA', 'EE'), ('ETHIOPIA', 'ET'), ('FALKLAND ISLANDS ', 'FK'), ('FAROE ISLANDS', 'FO'), ('FIJI', 'FJ'), ('FINLAND', 'FI'), ('FRANCE', 'FR'), ('FRENCH GUIANA', 'GF'), ('FRENCH POLYNESIA', 'PF'), ('FRENCH SOUTHERN TERRITORIES', 'TF'), ('GABON', 'GA'), ('GAMBIA', 'GM'), ('GEORGIA', 'GE'), ('GERMANY', 'DE'), ('GHANA', 'GH'), ('GIBRALTAR', 'GI'), ('GREECE', 'GR'), ('GREENLAND', 'GL'), ('GRENADA', 'GD'), ('GUADELOUPE', 'GP'), ('GUAM', 'GU'), ('GUATEMALA', 'GT'), ('GUINEA', 'GN'), ('GUINEA', 'GW'), ('GUYANA', 'GY'), ('HAITI', 'HT'), ('HEARD ISLAND AND MCDONALD ISLANDS', 'HM'), ('HONDURAS', 'HN'), ('HONG KONG', 'HK'), ('HUNGARY', 'HU'), ('ICELAND', 'IS'), ('INDIA', 'IN'), ('INDONESIA', 'ID'), ('IRAN, ISLAMIC REPUBLIC OF', 'IR'), ('IRAQ', 'IQ'), ('IRELAND', 'IE'), ('ISRAEL', 'IL'), ('ITALY', 'IT'), ('JAMAICA', 'JM'), ('JAPAN', 'JP'), ('JORDAN', 'JO'), ('KAZAKHSTAN', 'KZ'), ('KENYA', 'KE'), ('KIRIBATI', 'KI'), ("KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF", 'KP'), ('KOREA, REPUBLIC OF', 'KR'), ('KUWAIT', 'KW'), ('KYRGYZSTAN', 'KG'), ("LAO PEOPLE'S DEMOCRATIC REPUBLIC", 'LA'), ('LATVIA', 'LV'), ('LEBANON', 'LB'), ('LESOTHO', 'LS'), ('LIBERIA', 'LR'), ('LIBYAN ARAB JAMAHIRIYA', 'LY'), ('LIECHTENSTEIN', 'LI'), ('LITHUANIA', 'LT'), ('LUXEMBOURG', 'LU'), ('MACAO', 'MO'), ('NORTH MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'MK'), ('MADAGASCAR', 'MG'), ('MALAWI', 'MW'), ('MALAYSIA', 'MY'), ('MALDIVES', 'MV'), ('MALI', 'ML'), ('MALTA', 'MT'), ('MARSHALL ISLANDS', 'MH'), ('MARTINIQUE', 'MQ'), ('MAURITANIA', 'MR'), ('MAURITIUS', 'MU'), ('MAYOTTE', 'YT'), ('MEXICO', 'MX'), ('MICRONESIA, FEDERATED STATES OF', 'FM'), ('MOLDOVA, REPUBLIC OF', 'MD'), ('MONACO', 'MC'), ('MONGOLIA', 'MN'), ('MONTSERRAT', 'MS'), ('MOROCCO', 'MA'), ('MOZAMBIQUE', 'MZ'), ('MYANMAR', 'MM'), ('NAMIBIA', 'NA'), ('NAURU', 'NR'), ('NEPAL', 'NP'), ('NETHERLANDS', 'NL'), ('NETHERLANDS ANTILLES', 'AN'), ('NEW CALEDONIA', 'NC'), ('NEW ZEALAND', 'NZ'), ('NICARAGUA', 'NI'), ('NIGER', 'NE'), ('NIGERIA', 'NG'), ('NIUE', 'NU'), ('NORFOLK ISLAND', 'NF'), ('NORTHERN MARIANA ISLANDS', 'MP'), ('NORWAY', 'NO'), ('OMAN', 'OM'), ('PAKISTAN', 'PK'), ('PALAU', 'PW'), ('PALESTINIAN TERRITORY, OCCUPIED', 'PS'), ('PANAMA', 'PA'), ('PAPUA NEW GUINEA', 'PG'), ('PARAGUAY', 'PY'), ('PERU', 'PE'), ('PHILIPPINES', 'PH'), ('PITCAIRN', 'PN'), ('POLAND', 'PL'), ('PORTUGAL', 'PT'), ('PUERTO RICO', 'PR'), ('QATAR', 'QA'), ('RÃ‰UNION', 'RE'), ('ROMANIA', 'RO'), ('RUSSIAN FEDERATION', 'RU'), ('RWANDA', 'RW'), ('SAINT HELENA', 'SH'), ('SAINT KITTS AND NEVIS', 'KN'), ('SAINT LUCIA', 'LC'), ('SAINT PIERRE AND MIQUELON', 'PM'), ('SAINT VINCENT AND THE GRENADINES', 'VC'), ('SAMOA', 'WS'), ('SAN MARINO', 'SM'), ('SAO TOME AND PRINCIPE', 'ST'), ('SAUDI ARABIA', 'SA'), ('SENEGAL', 'SN'), ('SERBIA AND MONTENEGRO', 'CS'), ('SEYCHELLES', 'SC'), ('SIERRA LEONE', 'SL'), ('SINGAPORE', 'SG'), ('SLOVAKIA', 'SK'), ('SLOVENIA', 'SI'), ('SOLOMON ISLANDS', 'SB'), ('SOMALIA', 'SO'), ('SOUTH AFRICA', 'ZA'), ('SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS', 'GS'), ('SPAIN', 'ES'), ('SRI LANKA', 'LK'), ('SUDAN', 'SD'), ('SURINAME', 'SR'), ('SVALBARD AND JAN MAYEN', 'SJ'), ('SWAZILAND', 'SZ'), ('SWEDEN', 'SE'), ('SWITZERLAND', 'CH'), ('SYRIAN ARAB REPUBLIC', 'SY'), ('TAIWAN, PROVINCE OF CHINA', 'TW'), ('TAJIKISTAN', 'TJ'), ('TANZANIA, UNITED REPUBLIC OF', 'TZ'), ('THAILAND', 'TH'), ('TIMOR', 'TL'), ('TOGO', 'TG'), ('TOKELAU', 'TK'), ('TONGA', 'TO'), ('TRINIDAD AND TOBAGO', 'TT'), ('TUNISIA', 'TN'), ('TURKEY', 'TR'), ('TURKMENISTAN', 'TM'), ('TURKS AND CAICOS ISLANDS', 'TC'), ('TUVALU', 'TV'), ('UGANDA', 'UG'), ('UKRAINE', 'UA'), ('UNITED ARAB EMIRATES', 'AE'), ('UNITED KINGDOM', 'GB'), ('UNITED STATES', 'US'), ('UNITED STATES MINOR OUTLYING ISLANDS', 'UM'), ('URUGUAY', 'UY'), ('UZBEKISTAN', 'UZ'), ('VANUATU', 'VU'), ('VIET NAM', 'VN'), ('VIRGIN ISLANDS, BRITISH', 'VG'), ('VIRGIN ISLANDS, U.S.', 'VI'), ('WALLIS AND FUTUNA', 'WF'), ('WESTERN SAHARA', 'EH'), ('YEMEN', 'YE'), ('ZIMBABWE', 'ZW')], default=None, max_length=100)),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_id',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodies.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(choices=[('AFGHANISTAN', 'AF'), ('ALBANIA', 'AL'), ('ALGERIA', 'DZ'), ('AMERICAN SAMOA', 'AS'), ('ANDORRA', 'AD'), ('ANGOLA', 'AO'), ('ANGUILLA', 'AI'), ('ANTARCTICA', 'AQ'), ('ANTIGUA AND BARBUDA', 'AG'), ('ARGENTINA', 'AR'), ('ARMENIA', 'AM'), ('ARUBA', 'AW'), ('AUSTRALIA', 'AU'), ('AUSTRIA', 'AT'), ('AZERBAIJAN', 'AZ'), ('BAHAMAS', 'BS'), ('BAHRAIN', 'BH'), ('BANGLADESH', 'BD'), ('BARBADOS', 'BB'), ('BELARUS', 'BY'), ('BELGIUM', 'BE'), ('BELIZE', 'BZ'), ('BENIN', 'BJ'), ('BERMUDA', 'BM'), ('BHUTAN', 'BT'), ('BOLIVIA', 'BO'), ('BOSNIA AND HERZEGOVINA', 'BA'), ('BOTSWANA', 'BW'), ('BOUVET ISLAND', 'BV'), ('BRAZIL', 'BR'), ('BRITISH INDIAN OCEAN TERRITORY', 'IO'), ('BRUNEI DARUSSALAM', 'BN'), ('BULGARIA', 'BG'), ('BURKINA FASO', 'BF'), ('BURUNDI', 'BI'), ('CAMBODIA', 'KH'), ('CAMEROON', 'CM'), ('CANADA', 'CA'), ('CAPE VERDE', 'CV'), ('CAYMAN ISLANDS', 'KY'), ('CENTRAL AFRICAN REPUBLIC', 'CF'), ('CHAD', 'TD'), ('CHILE', 'CL'), ('CHINA', 'CN'), ('CHRISTMAS ISLAND', 'CX'), ('COCOS ISLANDS', 'CC'), ('COLOMBIA', 'CO'), ('COMOROS', 'KM'), ('CONGO', 'CG'), ('CONGO, THE DEMOCRATIC REPUBLIC OF', 'CD'), ('COOK ISLANDS', 'CK'), ('COSTA RICA', 'CR'), ("CÃ”TE D'IVOIRE", 'CI'), ('CROATIA', 'HR'), ('CUBA', 'CU'), ('CYPRUS', 'CY'), ('CZECH REPUBLIC', 'CZ'), ('DENMARK', 'DK'), ('DJIBOUTI', 'DJ'), ('DOMINICA', 'DM'), ('DOMINICAN REPUBLIC', 'DO'), ('ECUADOR', 'EC'), ('EGYPT', 'EG'), ('EL SALVADOR', 'SV'), ('EQUATORIAL GUINEA', 'GQ'), ('ERITREA', 'ER'), ('ESTONIA', 'EE'), ('ETHIOPIA', 'ET'), ('FALKLAND ISLANDS ', 'FK'), ('FAROE ISLANDS', 'FO'), ('FIJI', 'FJ'), ('FINLAND', 'FI'), ('FRANCE', 'FR'), ('FRENCH GUIANA', 'GF'), ('FRENCH POLYNESIA', 'PF'), ('FRENCH SOUTHERN TERRITORIES', 'TF'), ('GABON', 'GA'), ('GAMBIA', 'GM'), ('GEORGIA', 'GE'), ('GERMANY', 'DE'), ('GHANA', 'GH'), ('GIBRALTAR', 'GI'), ('GREECE', 'GR'), ('GREENLAND', 'GL'), ('GRENADA', 'GD'), ('GUADELOUPE', 'GP'), ('GUAM', 'GU'), ('GUATEMALA', 'GT'), ('GUINEA', 'GN'), ('GUINEA', 'GW'), ('GUYANA', 'GY'), ('HAITI', 'HT'), ('HEARD ISLAND AND MCDONALD ISLANDS', 'HM'), ('HONDURAS', 'HN'), ('HONG KONG', 'HK'), ('HUNGARY', 'HU'), ('ICELAND', 'IS'), ('INDIA', 'IN'), ('INDONESIA', 'ID'), ('IRAN, ISLAMIC REPUBLIC OF', 'IR'), ('IRAQ', 'IQ'), ('IRELAND', 'IE'), ('ISRAEL', 'IL'), ('ITALY', 'IT'), ('JAMAICA', 'JM'), ('JAPAN', 'JP'), ('JORDAN', 'JO'), ('KAZAKHSTAN', 'KZ'), ('KENYA', 'KE'), ('KIRIBATI', 'KI'), ("KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF", 'KP'), ('KOREA, REPUBLIC OF', 'KR'), ('KUWAIT', 'KW'), ('KYRGYZSTAN', 'KG'), ("LAO PEOPLE'S DEMOCRATIC REPUBLIC", 'LA'), ('LATVIA', 'LV'), ('LEBANON', 'LB'), ('LESOTHO', 'LS'), ('LIBERIA', 'LR'), ('LIBYAN ARAB JAMAHIRIYA', 'LY'), ('LIECHTENSTEIN', 'LI'), ('LITHUANIA', 'LT'), ('LUXEMBOURG', 'LU'), ('MACAO', 'MO'), ('NORTH MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'MK'), ('MADAGASCAR', 'MG'), ('MALAWI', 'MW'), ('MALAYSIA', 'MY'), ('MALDIVES', 'MV'), ('MALI', 'ML'), ('MALTA', 'MT'), ('MARSHALL ISLANDS', 'MH'), ('MARTINIQUE', 'MQ'), ('MAURITANIA', 'MR'), ('MAURITIUS', 'MU'), ('MAYOTTE', 'YT'), ('MEXICO', 'MX'), ('MICRONESIA, FEDERATED STATES OF', 'FM'), ('MOLDOVA, REPUBLIC OF', 'MD'), ('MONACO', 'MC'), ('MONGOLIA', 'MN'), ('MONTSERRAT', 'MS'), ('MOROCCO', 'MA'), ('MOZAMBIQUE', 'MZ'), ('MYANMAR', 'MM'), ('NAMIBIA', 'NA'), ('NAURU', 'NR'), ('NEPAL', 'NP'), ('NETHERLANDS', 'NL'), ('NETHERLANDS ANTILLES', 'AN'), ('NEW CALEDONIA', 'NC'), ('NEW ZEALAND', 'NZ'), ('NICARAGUA', 'NI'), ('NIGER', 'NE'), ('NIGERIA', 'NG'), ('NIUE', 'NU'), ('NORFOLK ISLAND', 'NF'), ('NORTHERN MARIANA ISLANDS', 'MP'), ('NORWAY', 'NO'), ('OMAN', 'OM'), ('PAKISTAN', 'PK'), ('PALAU', 'PW'), ('PALESTINIAN TERRITORY, OCCUPIED', 'PS'), ('PANAMA', 'PA'), ('PAPUA NEW GUINEA', 'PG'), ('PARAGUAY', 'PY'), ('PERU', 'PE'), ('PHILIPPINES', 'PH'), ('PITCAIRN', 'PN'), ('POLAND', 'PL'), ('PORTUGAL', 'PT'), ('PUERTO RICO', 'PR'), ('QATAR', 'QA'), ('RÃ‰UNION', 'RE'), ('ROMANIA', 'RO'), ('RUSSIAN FEDERATION', 'RU'), ('RWANDA', 'RW'), ('SAINT HELENA', 'SH'), ('SAINT KITTS AND NEVIS', 'KN'), ('SAINT LUCIA', 'LC'), ('SAINT PIERRE AND MIQUELON', 'PM'), ('SAINT VINCENT AND THE GRENADINES', 'VC'), ('SAMOA', 'WS'), ('SAN MARINO', 'SM'), ('SAO TOME AND PRINCIPE', 'ST'), ('SAUDI ARABIA', 'SA'), ('SENEGAL', 'SN'), ('SERBIA AND MONTENEGRO', 'CS'), ('SEYCHELLES', 'SC'), ('SIERRA LEONE', 'SL'), ('SINGAPORE', 'SG'), ('SLOVAKIA', 'SK'), ('SLOVENIA', 'SI'), ('SOLOMON ISLANDS', 'SB'), ('SOMALIA', 'SO'), ('SOUTH AFRICA', 'ZA'), ('SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS', 'GS'), ('SPAIN', 'ES'), ('SRI LANKA', 'LK'), ('SUDAN', 'SD'), ('SURINAME', 'SR'), ('SVALBARD AND JAN MAYEN', 'SJ'), ('SWAZILAND', 'SZ'), ('SWEDEN', 'SE'), ('SWITZERLAND', 'CH'), ('SYRIAN ARAB REPUBLIC', 'SY'), ('TAIWAN, PROVINCE OF CHINA', 'TW'), ('TAJIKISTAN', 'TJ'), ('TANZANIA, UNITED REPUBLIC OF', 'TZ'), ('THAILAND', 'TH'), ('TIMOR', 'TL'), ('TOGO', 'TG'), ('TOKELAU', 'TK'), ('TONGA', 'TO'), ('TRINIDAD AND TOBAGO', 'TT'), ('TUNISIA', 'TN'), ('TURKEY', 'TR'), ('TURKMENISTAN', 'TM'), ('TURKS AND CAICOS ISLANDS', 'TC'), ('TUVALU', 'TV'), ('UGANDA', 'UG'), ('UKRAINE', 'UA'), ('UNITED ARAB EMIRATES', 'AE'), ('UNITED KINGDOM', 'GB'), ('UNITED STATES', 'US'), ('UNITED STATES MINOR OUTLYING ISLANDS', 'UM'), ('URUGUAY', 'UY'), ('UZBEKISTAN', 'UZ'), ('VANUATU', 'VU'), ('VIET NAM', 'VN'), ('VIRGIN ISLANDS, BRITISH', 'VG'), ('VIRGIN ISLANDS, U.S.', 'VI'), ('WALLIS AND FUTUNA', 'WF'), ('WESTERN SAHARA', 'EH'), ('YEMEN', 'YE'), ('ZIMBABWE', 'ZW')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='foodies.user_account'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='foodies.user_account'),
        ),
    ]