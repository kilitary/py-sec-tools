rule _Shrinker_3_2_obqbia
{
	meta:
		description = "Shrinker 3_2"
	strings:
		$a = {558BEC565775656800010000E8F1E6FFFF83C404}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
