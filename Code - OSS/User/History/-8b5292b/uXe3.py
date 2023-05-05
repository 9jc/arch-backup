print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
        s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
        s.num_peers, s.state), end=' ')

    
    progressw = (s.progress)
    downloadrt = (s.download_rate)
    uploadrt = (s.upload_rate)
    numpeers = (s.num_peers)
    print(s.state)
    xf = add_suffix(val=downloadrt)
    info = lt.torrent_info() 
    print(info)
    print("-----------------------")
    print(xsf)
    print(xdf)
    print(f"progress = {progressw}")
    print(f"upload = {uploadrt}")
    print(f"peers = {numpeers}")
    print(xf)
    # print(state_str)
    time.sleep(1)
