rule _ICE_Archive_rotxua
{
	meta:
		description = "ICE Archive"
	strings:
		$a = {????2D6C68??2D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
