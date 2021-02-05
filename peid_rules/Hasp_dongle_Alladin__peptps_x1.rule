rule _Hasp_dongle_Alladin__peptps
{
	meta:
		description = "Hasp dongle _Alladin_"
	strings:
		$a = {5053515257568B751C8B3E??????????8B5D088AFB????035D108B450C8B4D148B551880FF32}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
