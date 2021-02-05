rule _Go32Stub_v_2_00_DOS_Extender_tlsykk
{
	meta:
		description = "Go32Stub v_2_00 DOS_Extender"
	strings:
		$a = {0E1F8C1E????8C06????FCB430CD2180}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
