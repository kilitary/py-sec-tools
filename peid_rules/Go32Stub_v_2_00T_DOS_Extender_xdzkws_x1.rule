rule _Go32Stub_v_2_00T_DOS_Extender_xdzkws
{
	meta:
		description = "Go32Stub v_2_00T DOS_Extender"
	strings:
		$a = {0E1F8C1E????8C06????FCB430CD213C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
