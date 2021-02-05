rule _Shrinker_v3_2_hvqprm
{
	meta:
		description = "Shrinker v3_2"
	strings:
		$a = {833D??????????558BEC56577565680001????E8??E6FFFF83C4048B7508A3????????85F6741D68FF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
