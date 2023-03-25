#manifest that kills a process named killmenow

service{'pkill' :
        command => '/usr/bin/pkill -9 killmenow'
}
