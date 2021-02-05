rule _Exe_Shield_v2_7_gulhde
{
	meta:
		description = "Exe Shield v2_7"
	strings:
		$a = {EB0668C39C60E85D555B81ED8B85018566C785}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
