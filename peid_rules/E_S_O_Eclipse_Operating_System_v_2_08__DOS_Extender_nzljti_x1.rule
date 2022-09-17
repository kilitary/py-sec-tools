rule _E_S_O_Eclipse_Operating_System_v_2_08__DOS_Extender_nzljti
{
	meta:
		description = "E_S_O_ Eclipse Operating System v_2_08 _ DOS Extender"
	strings:
		$a = {8CC88ED8BA????E8????BB????8CC02BD8B44ACD21BA????73??E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
