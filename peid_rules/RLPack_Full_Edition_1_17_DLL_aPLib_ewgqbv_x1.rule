rule _RLPack_Full_Edition_1_17_DLL_aPLib_ewgqbv
{
	meta:
		description = "RLPack Full Edition 1_17 DLL _aPLib"
	strings:
		$a = {807C2408010F85????????60E8000000008B2C2483C4048DB5530300008D9D0202000033FFE8????????EB0FFF743704FF3437FFD383C40883C708833C370075}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
