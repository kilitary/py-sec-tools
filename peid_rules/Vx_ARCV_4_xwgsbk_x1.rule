rule _Vx_ARCV_4_xwgsbk
{
	meta:
		description = "Vx_ ARCV_4"
	strings:
		$a = {E800005D81ED060181FC4F50740B8DB68601BF000157A4EB111E06}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
