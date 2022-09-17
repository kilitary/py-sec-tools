rule _Armadillo_V5_40__Silicon_Realms_Toolworks__Sign_By_fly__20080214_xgjszg
{
	meta:
		description = "Armadillo V5_40 __ Silicon Realms Toolworks _ Sign_By_fly _ 20080214"
	strings:
		$a = {E8933E0000E916FEFFFF6A0C68????????E8B41F00008B4D0833FF3BCF762E6AE05833D2F7F13B450C1BC040751FE8AF1D0000C7000C0000005757575757E8401D000083C41433C0E9D50000000FAF4D0C8BF18975}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
