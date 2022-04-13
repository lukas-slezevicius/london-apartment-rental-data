import csv
import requests
import time
import dataclasses


def get_area_list() -> list[str]:
    r = requests.get("https://api.findmyarea.co.uk:5001/api/all_area_names")
    if not r.ok:
        raise RuntimeError
    return list(r.json().keys())


@dataclasses.dataclass
class Area:
    name: str
    zoopla_name: str
    latitude: float
    longitude: float
    post_code_area: str
    commute_city_min: float
    commute_city_max: float
    commute_oxford_circus_min: float
    commute_oxford_circus_max: float
    commute_waterloo_min: float
    commute_waterloo_max: float
    lower_quartile_studio_rent: int | None
    median_studio_rent: int | None
    upper_quartile_studio_rent: int | None
    lower_quartile_one_bedroom_rent: int | None
    median_one_bedroom_rent: int | None
    upper_quartile_one_bedroom_rent: int | None
    aldi_count: int
    asda_count: int
    bakery_count: int
    bar_count: int
    british_resuarant_count: int
    chinese_restaurant_count: int
    cinema_count: int
    french_restaurant_count: int
    gymbox_count: int
    indian_restaurant_count: int
    italian_restaurant_count: int
    japanese_restaurant_count: int
    lidl_count: int
    morrisons_count: int
    museum_count: int
    nightclub_count: int
    pub_count: int
    sainsburys_count: int
    tesco_count: int
    thai_restaurant_count: int
    theater_count: int
    waitrose_count: int
    gym_count: int
    park_count: int
    age_19_minus_perc: float
    age_20s_perc: float
    age_30s_perc: float
    age_40_plus_perc: float
    average_household_income: float
    very_good_health_perc: float


def int_or_none(v: str | None) -> int | None:
    if v is None:
        return v
    return int(v)


def get_area_data(area_name: str) -> Area:
    r = requests.get(
        "https://api.findmyarea.co.uk:5001/api/single_area_stats?area={}".format(
            area_name
        )
    )
    if not r.ok:
        raise RuntimeError
    stats = r.json()["stats"]
    return Area(
        name=area_name,
        zoopla_name=stats["property_rent_area_data"][area_name]["zoopla_name"],
        latitude=float(stats["qualifying_area_basics_data"][0]["latitude"]),
        longitude=float(stats["qualifying_area_basics_data"][0]["longitude"]),
        post_code_area=stats["postcode_data"]["postcode_area"],
        commute_city_min=float(
            stats["commute_area_data"][area_name]["lowest_commute_time0"]
        ),
        commute_city_max=float(
            stats["commute_area_data"][area_name]["highest_commute_time0"]
        ),
        commute_oxford_circus_min=float(
            stats["commute_area_data"][area_name]["lowest_commute_time1"]
        ),
        commute_oxford_circus_max=float(
            stats["commute_area_data"][area_name]["highest_commute_time1"]
        ),
        commute_waterloo_min=float(
            stats["commute_area_data"][area_name]["lowest_commute_time2"]
        ),
        commute_waterloo_max=float(
            stats["commute_area_data"][area_name]["highest_commute_time2"]
        ),
        lower_quartile_studio_rent=int_or_none(
            stats["property_rent_area_data"][area_name].get(
                "lower_quartile_price_0_bedrooms"
            )
        ),
        median_studio_rent=int_or_none(
            stats["property_rent_area_data"][area_name].get("median_price_0_bedrooms")
        ),
        upper_quartile_studio_rent=int_or_none(
            stats["property_rent_area_data"][area_name].get(
                "upper_quartile_price_0_bedrooms"
            )
        ),
        lower_quartile_one_bedroom_rent=int_or_none(
            stats["property_rent_area_data"][area_name].get(
                "lower_quartile_price_1_bedrooms"
            )
        ),
        median_one_bedroom_rent=int_or_none(
            stats["property_rent_area_data"][area_name].get("median_price_1_bedrooms")
        ),
        upper_quartile_one_bedroom_rent=int_or_none(
            stats["property_rent_area_data"][area_name].get(
                "upper_quartile_price_1_bedrooms"
            )
        ),
        aldi_count=int(
            stats["tags_area_data_optional"]["aldi"][area_name]["amenity_count"]
        ),
        asda_count=int(
            stats["tags_area_data_optional"]["asda"][area_name]["amenity_count"]
        ),
        bakery_count=int(
            stats["tags_area_data_optional"]["bakeries"][area_name]["amenity_count"]
        ),
        bar_count=int(
            stats["tags_area_data_optional"]["bars"][area_name]["amenity_count"]
        ),
        british_resuarant_count=int(
            stats["tags_area_data_optional"]["british_restaurants"][area_name][
                "amenity_count"
            ]
        ),
        chinese_restaurant_count=int(
            stats["tags_area_data_optional"]["chinese_restaurants"][area_name][
                "amenity_count"
            ]
        ),
        cinema_count=int(
            stats["tags_area_data_optional"]["cinema"][area_name]["amenity_count"]
        ),
        french_restaurant_count=int(
            stats["tags_area_data_optional"]["french_restaurants"][area_name][
                "amenity_count"
            ]
        ),
        gymbox_count=int(
            stats["tags_area_data_optional"]["gymbox"][area_name]["amenity_count"]
        ),
        indian_restaurant_count=int(
            stats["tags_area_data_optional"]["indian_restaurants"][area_name][
                "amenity_count"
            ]
        ),
        italian_restaurant_count=int(
            stats["tags_area_data_optional"]["italian_restaurants"][area_name][
                "amenity_count"
            ]
        ),
        japanese_restaurant_count=int(
            stats["tags_area_data_optional"]["japanese_restaurants"][area_name][
                "amenity_count"
            ]
        ),
        lidl_count=int(
            stats["tags_area_data_optional"]["lidl"][area_name]["amenity_count"]
        ),
        morrisons_count=int(
            stats["tags_area_data_optional"]["morrisons"][area_name]["amenity_count"]
        ),
        museum_count=int(
            stats["tags_area_data_optional"]["museum"][area_name]["amenity_count"]
        ),
        nightclub_count=int(
            stats["tags_area_data_optional"]["nightclub"][area_name]["amenity_count"]
        ),
        pub_count=int(
            stats["tags_area_data_optional"]["pubs"][area_name]["amenity_count"]
        ),
        sainsburys_count=int(
            stats["tags_area_data_optional"]["sainsburys"][area_name]["amenity_count"]
        ),
        tesco_count=int(
            stats["tags_area_data_optional"]["tesco"][area_name]["amenity_count"]
        ),
        thai_restaurant_count=int(
            stats["tags_area_data_optional"]["thai_restaurants"][area_name][
                "amenity_count"
            ]
        ),
        theater_count=int(
            stats["tags_area_data_optional"]["theatre"][area_name]["amenity_count"]
        ),
        waitrose_count=int(
            stats["tags_area_data_optional"]["waitrose"][area_name]["amenity_count"]
        ),
        gym_count=sum(
            stats["tags_area_data_optional"][gym_name][area_name]["amenity_count"]
            for gym_name in (
                "fitness_first",
                "gymbox",
                "nuffield_health",
                "pure_gym",
                "virgin_active",
            )
        ),
        park_count=len(
            stats["tags_area_data_optional"]["plentiful_green_spaces"][area_name][
                "green_spaces"
            ]
        ),
        age_19_minus_perc=round(
            float(
                stats["demographics_area_data_optional"][area_name][
                    "age_19_minus_demographic_score"
                ]
            ),
            2,
        ),
        age_20s_perc=round(
            float(
                stats["demographics_area_data_optional"][area_name][
                    "age_20s_demographic_score"
                ]
            ),
            2,
        ),
        age_30s_perc=round(
            float(
                stats["demographics_area_data_optional"][area_name][
                    "age_30s_demographic_score"
                ]
            ),
            2,
        ),
        age_40_plus_perc=round(
            float(
                stats["demographics_area_data_optional"][area_name][
                    "age_40_plus_demographic_score"
                ]
            ),
            2,
        ),
        average_household_income=round(
            float(
                stats["demographics_area_data_optional"][area_name][
                    "household_income_demographic_score"
                ]
            ),
            2,
        ),
        very_good_health_perc=round(
            float(
                stats["demographics_area_data_optional"][area_name][
                    "very_good_health_demographic_score"
                ]
            ),
            2,
        ),
    )


def save_areas_to_csv(areas: list[Area]):
    with open("find-my-area-co-uk.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=dataclasses.asdict(areas[0]))
        writer.writeheader()
        for area in areas:
            writer.writerow(dataclasses.asdict(area))


def main():
    print("Collecting area data from findmyarea.co.uk")
    area_names = get_area_list()
    areas: list[Area] = []
    # Skip areas that don't have data (the website has bugs)
    skip_list = {"manor_house"}
    for i, area_name in enumerate(area_names):
        if area_name in skip_list:
            print("Skipping", area_name)
            continue
        areas.append(get_area_data(area_name))
        print(f"{i+1}/{len(area_names)} done")
        time.sleep(1 / 3)
    print("Writing data to CSV file")
    save_areas_to_csv(areas)
    print("Finished writing CSV file")


if __name__ == "__main__":
    main()
