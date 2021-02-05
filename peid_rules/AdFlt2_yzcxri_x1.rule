rule _AdFlt2_yzcxri
{
	meta:
		description = "AdFlt2"
	strings:
		$a = {6800019C0FA00FA860FD6A000FA1BE????AD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
