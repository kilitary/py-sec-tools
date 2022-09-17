rule _Shrinker_3_4_wekfka
{
	meta:
		description = "Shrinker 3_4"
	strings:
		$a = {558BEC5657756B6800010000E8110B000083C404}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
